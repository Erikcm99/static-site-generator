from typing import Dict, List
class HTMLNode():
    def __init__(self, tag = None,value = None,children: List | None = None,props:Dict[str,str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        if len(self.props) > 0:
            result = ''
            for k,v in self.props.items():
                result += f' {k}="{v}"'
            return result
        return ""

    def __repr__(self):
        return f"HTMLNode(tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"


