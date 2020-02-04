import xml.etree.ElementTree
import json



def children (root):
    list_of_children = []
    for i in list(root):
        list_of_children.append(i.tag)
    return list_of_children


def make_dict_from_tree(element_tree):
    def internal_iter(tree, tmp):
        global count
        count = 0
        if tree is None:
            return tmp

        if list(tree):
            tmp[tree.tag] = {}
            for each in list(tree):
                result = internal_iter(each, {})
                if each.tag in tmp[tree.tag]:
                    if not isinstance(accum[tree.tag][each.tag], list):
                        tmp[tree.tag][each.tag] = children(accum[tree.tag])

                    tmp[tree.tag][each.tag].append(result[each.tag])
                else:
                    count += 1
                    tmp[tree.tag].update(result)
        else:
            tmp[tree.tag] = tree.text

        return tmp

    return internal_iter(element_tree, {})

def main():
    xml_string = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
    print(json.dumps(make_dict_from_tree(xml.etree.ElementTree.fromstring(xml_string)), indent=1), ',', count)


main()