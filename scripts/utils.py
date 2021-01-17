import json

from generator import Generator


def make_activities_file(sql_file, gpx_dir, json_file):
    generator = Generator(sql_file)
    generator.sync_from_gpx(gpx_dir)
    activities_list = generator.loadForMapping()
    with open(json_file, "w") as f:
        f.write("const activities = ")
        json.dump(activities_list, f, indent=2)
        f.write(";\n")
        f.write("\n")
        f.write("export {activities};\n")

def make_activities_file_only(sql_file, json_file):
    generator = Generator(sql_file)
    activities_list = generator.loadForMapping()
    with open(json_file, "w") as f:
        json.dump(activities_list, f)
