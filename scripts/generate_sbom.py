import json
from packageurl import PackageURL
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output.json import JsonV1Dot4

def build_sbom():
    print("Parsing manifest dependencies...")
    bom = Bom()
    
    with open("requirements.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line and "==" in line:
                name, version = line.split("==")
                purl_obj = PackageURL(type='pypi', name=name, version=version)
                comp = Component(
                    name=name,
                    version=version,
                    type=ComponentType.LIBRARY,
                    purl=purl_obj
                )
                bom.components.add(comp)
                
    output = JsonV1Dot4(bom).output_as_string()
    with open("bom.json", "w") as out_file:
        out_file.write(output)
    print("Success: Generated machine-readable bom.json artifact flawlessly.")

if __name__ == "__main__":
    build_sbom()
