from os import path as os_path, makedirs, getcwd, sep, walk
from sys import path as sys_path
from templates import CONF_TEMPLATE, INDEX_CONTENT
from sphinx.application import Sphinx
from sphinx.ext.apidoc import main as apidoc_main


class AutoSphinxGenerator:

    def __init__(self, configs: dict) -> None:
        self.project_name = configs.get("project_name")
        self.repo_path = configs.get("repo_path")
        self.exclude = configs.get("exclude", [])
        self.project_dir = os_path.join(getcwd(), self.project_name)
        self.source_dir = os_path.join(self.project_dir, "docs", "source")
        self.build_dir = os_path.join(self.project_dir, "docs", "build")
        self.conf_path = self.source_dir

    def init(self) -> None:
        if not os_path.exists(self.source_dir):
            makedirs(self.source_dir, exist_ok=True)
        if not os_path.exists(self.build_dir):
            makedirs(self.build_dir, exist_ok=True)

        # formatted_excludes = [f"'{item}'" for item in self.exclude]
        # print(formatted_excludes)

        conf_content = CONF_TEMPLATE.format(repo_path=self.repo_path, project_name=self.project_name, excluded=self.exclude)

        with open(os_path.join(self.source_dir, "conf.py"), 'w') as cf:
            cf.write(conf_content)
    
    def generate_docs(self) -> None:

        index_content = INDEX_CONTENT.format(project_name=self.project_name)

        with open(os_path.join(self.source_dir, "index.rst"), 'w') as f:
            f.write(index_content)
    

    def generate_apidoc(self) -> None:


        apidoc_args = [
            '--output-dir', self.source_dir,  # Output directory for generated .rst files
            '--module-first',  # Modules come first in the ToC
            '--force',  # Overwrite existing files
            '--no-toc',  # Don't generate the ToC in the individual files
            self.repo_path
        ]

        # Run sphinx-apidoc programmatically
        apidoc_main(apidoc_args)


    def build_html(self) -> None:
        app = Sphinx(
            srcdir=self.source_dir,
            confdir=self.conf_path,
            outdir=os_path.join(self.build_dir, "html"),
            doctreedir=os_path.join(self.build_dir, "doctrees"),
            buildername="html"
        )
        app.build()

    def run(self) -> None:
        print(f"Initializing {self.__class__.__name__} for project '{self.project_name}'")
        self.init()

        print("Generating docs...")
        self.generate_docs()

        print("Generating API docs using sphinx-apidoc...")
        self.generate_apidoc()

        print("Building HTML documentation...")
        self.build_html()

        print(f"Docs generated in {os_path.join(self.build_dir, 'html')}")