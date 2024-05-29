#!/usr/bin/python3
"""Serialize to XML and deserialyze to python Module"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML
    and save it to the given filename"""
    root = ET.Element("data")  # Create the root element
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = value  # Add each key-value pair

    tree = ET.ElementTree(root)  # Create an ElementTree object
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """read the XML data from that file,
    and return a deserialized Python dictionary"""

    # Parse the XML file and get the root element
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}

    for element in root:
        # Get the tag name of the element
        tag = element.tag
        # Get the text content of the element
        text = element.text
        # Add the tag and text to the result dictionary
        result_dict[tag] = text

    return result_dict
