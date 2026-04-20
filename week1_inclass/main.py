from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

# Define path to the XML metadata file
xml_path = Path("data/metadata/climate_dataset_dublin_core.xml")

# Show absolute path for verification/debugging
print("Metadata path:", xml_path.resolve())

# Check if file exists before further processing
print(" \n File exists:", xml_path.exists())



raw_xml = xml_path.read_text(encoding="utf-8")
print(raw_xml[:1500])



# Parse XML file into a tree structure
tree = ET.parse(xml_path)

# Access the root element 
root = tree.getroot()

# Show XML structure
print(ET.tostring(root, encoding="unicode"))

# Show the main tag of the XML
print("Root tag:", root.tag)

# Count only the first-level child elements
print("Number of direct child elements:", len(list(root)))
# Show full XML content as a string




fair_view = pd.DataFrame(
    [
        {"FAIR_principle": "Findable", "Relevant_fields": "title, subject, identifier", "Comment": "The dataset can be discovered and referenced more easily."},
        {"FAIR_principle": "Accessible", "Relevant_fields": "identifier", "Comment": "Accessibility depends on whether the identifier resolves to an accessible record."},
        {"FAIR_principle": "Interoperable", "Relevant_fields": "standardized XML structure, format", "Comment": "Structured metadata improves machine processing."},
        {"FAIR_principle": "Reusable", "Relevant_fields": "creator, description, date, format", "Comment": "Contextual fields help others understand and reuse the data."},
    ]
)

print(fair_view)




weaknesses = [
    "No explicit license field shown in this simple Dublin Core example.",
    "The description may still be too short for full reuse.",
    "Subject terms may need to be richer and more standardized.",
    "No explicit version or provenance field is included.",
]

for i, item in enumerate(weaknesses, start=1):
    print(f"{i}. {item}")