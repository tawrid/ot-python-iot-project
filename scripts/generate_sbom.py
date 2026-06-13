import json
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output.json import JsonV1Dot4

def build_sbom():
    print("Parsing manifest dependencies...")
    bom = Bom()
    
    # Read the explicit requirements inventory
    with open("requirements.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line and "==" in line:
                name, version = line.split("==")
                # Structure the programmatic CycloneDX component object mapping
                comp = Component(
                    name=name,
                    version=version,
                    type=ComponentType.LIBRARY,
                    purl=f"pkg:pypi/{name}@{version}"
                )
                bom.components.add(comp)
                
    # Serialize the inventory straight to machine-readable JSON formats
    output = JsonV1Dot4(bom).output_as_string()
    with open("bom.json", "w") as out_file:
        out_file.write(output)
    print("Success: Generated machine-readable bom.json artifact flawlessly.")

if __name__ == "__main__":
    build_sbom()
