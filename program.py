import json
import yaml
import xmltodict
import argparse

def xml_to_json(xml_path, json_path):

    try:
        xml_file = open(xml_path)
        try:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            json_file = open(json_path, 'w')
            json_file.write(json_data)
            json_file.close()
        except:
            print('xml file is not in proper format')
        xml_file.close()  
    except OSError:
        print('xml file not found')

def xml_to_yml(xml_path, yml_path):

    try:
        xml_file = open(xml_path)
        try:
            data_dict = xmltodict.parse(xml_file.read())
            yml_file = open(yml_path, 'w')
            yaml.dump(data_dict, yml_file)
            yml_file.close()
        except:
            print('xml file is not in proper format')
        xml_file.close()  
    except OSError:
        print('xml file not found')

def json_to_xml(json_path, xml_path):

    try:
        json_file = open(json_path)
        try:
            data_dict = json.loads(json_file.read())
            xml_file = open(xml_path, 'w')
            xmltodict.unparse(data_dict, xml_file)
            xml_file.close()
        except:
            print('json file is not in proper format')
        json_file.close()  
    except OSError:
        print('json file not found')

def json_to_yml(json_path, yml_path):

    try:
        json_file = open(json_path)
        try:
            data_dict = json.loads(json_file.read())
            yml_file = open(yml_path, 'w')
            yaml.dump(data_dict, yml_file)
            yml_file.close()
        except:
            print('json file is not in proper format')
        json_file.close()  
    except OSError:
        print('json file not found')

def yml_to_xml(yml_path, xml_path):

    try:
        yml_file = open(yml_path)
        try:
            data_dict = yaml.load(yml_file, yaml.SafeLoader)
            xml_file = open(xml_path, 'w')
            xmltodict.unparse(data_dict, xml_file)
            xml_file.close()
        except:
            print('yml file is not in proper format')
        yml_file.close()  
    except OSError:
        print('yml file not found')

def yml_to_json(yml_path, json_path):

    try:
        yml_file = open(yml_path)
        try:
            data_dict = yaml.load(yml_file, yaml.SafeLoader)
            json_data = json.dumps(data_dict)
            json_file = open(json_path, 'w')
            json_file.write(json_data)
            json_file.close()
        except:
            print('yml file is not in proper format')
        yml_file.close()  
    except OSError:
        print('yml file not found')

if __name__ == '__main__':
    xml_path = 'xml_file.xml'
    yml_path = 'yml_file.yml'
    json_path = 'json_file.json'

    parser = argparse.ArgumentParser()
    parser.add_argument('first_file_path', type=str)
    parser.add_argument('second_file_path', type=str)
    args = parser.parse_args()
    first_path, second_path = args.first_file_path, args.second_file_path

    first_path_extension = first_path[-4:]
    second_path_extenstion = second_path[-4:]

    if first_path_extension == 'json':
        if second_path_extenstion == '.xml':
            json_to_xml(first_path, second_path)
        elif second_path_extenstion == '.yml' or second_path_extenstion == 'yaml':
            json_to_yml(first_path, second_path)
        else:
            print('Second file extenstion not recognised')
    elif first_path_extension == '.xml':
        if second_path_extenstion == 'json':
            xml_to_json(first_path, second_path)
        elif second_path_extenstion == '.yml' or second_path_extenstion == 'yaml':
            xml_to_yml(first_path, second_path)
        else:
            print('Second file extenstion not recognised')
    elif first_path_extension == '.yml' or second_path_extenstion == 'yaml':
        if second_path_extenstion == 'json':
            yml_to_json(first_path, second_path)
        elif second_path_extenstion == '.xml':
            yml_to_xml(first_path, second_path)
        else:
            print('Second file extenstion not recognised')
    else:
        print('First file extenstion not recognised')
