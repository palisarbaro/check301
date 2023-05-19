def load_and_parse_file(filename):
    ids = []
    with open(filename) as f:
        for line in f:
            id_str = line.split('`id` = ')[1].replace(";", "").strip()
            ids.append(int(id_str.replace("'", "")))
    return ids

def load_and_parse_file2(filename):
    col1 = []
    col2 = []
    with open(filename) as f:
        for line in f:
            values = line.replace("INSERT INTO `seo_redirect` VALUES(", "").replace(");", "").split(",")
            if(values):
                col1.append(int(values[0].replace("'", "")))
                col2.append(int(values[1].replace("'", "")))
    return col1, col2

ids = load_and_parse_file("updateposts.sql")
ids_from, ids_to = load_and_parse_file2("redirectposts.sql")

print(len(set(ids)-set(ids_from)))
