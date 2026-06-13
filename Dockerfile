# Use a highly minimal, locked-down baseline image to minimize vulnerable surfaces
FROM python:3.10-alpine

# Set defensive configuration environment options
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create an unprivileged system group and user to prevent root escalation vectors
RUN addgroup -S otgroup && adduser -S otuser -G otgroup

# Install core system dependencies cleanly using alpine package management
RUN apk add --no-cache libffi-dev openssl-dev

# Stage application execution requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source repository contents safely into place
COPY src/ ./src/

# Hand over process folder ownership directly to our non-root system identity
RUN chown -R otuser:otgroup /app

# Demote running context execution space to non-privileged workspace profile
USER otuser

# Define the isolated runtime execution trigger
CMD ["python", "src/main.py"]
