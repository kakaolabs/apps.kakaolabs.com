class DataReader(object):
    def __init__(self, filepath):
        self.lines = open(filepath).readlines()
        self.contents = {}

    def add_content_to_category(self, category, content):
        if category not in self.contents:
            self.contents[category] = []
        self.contents[category].append(content)

    def parse(self):
        category = []
        content = None

        for line in self.lines:
            if line.startswith("#"):
                category = line[1:].strip()
                content = []
            elif line.strip() == '':
                if content:
                    self.add_content_to_category(category, '\n'.join(content))
                    content = []
            else:
                strip_line = line.strip()
                if strip_line:
                    content.append(strip_line)

        if content:
            self.add_content_to_category(category, '\n'.join(content))
