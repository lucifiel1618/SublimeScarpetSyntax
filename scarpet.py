import sublime
import sublime_plugin

from pathlib import Path
import logging

logger = logging.getLogger('scarpet')

NAME = "Scarpet"
# VERSION = "1.2.0"

PACKAGE_FOLDER = Path(sublime.packages_path(), 'User', NAME)
PACKAGE_SCHEME_FOLDER = PACKAGE_FOLDER/'Schemes'
TEMPLATE_SCHEME = PACKAGE_SCHEME_FOLDER/'Template.sublime-color-scheme'
SCARPET_SETTINGS = sublime.load_settings('scarpet.sublime-settings')

def current_scheme() -> Path:
    return Path(sublime.find_resources(sublime.ui_info()['color_scheme']['value'])[0])

class ScarpetEventListener(sublime_plugin.EventListener):
    def on_init(self, views: 'list[sublime.View]') -> None:
        if not TEMPLATE_SCHEME.exists():
            if not PACKAGE_FOLDER.exists():
                PACKAGE_FOLDER.mkdir()
            if not PACKAGE_SCHEME_FOLDER.exists():
                PACKAGE_SCHEME_FOLDER.mkdir()
 
            scheme_content = sublime.load_binary_resource('Packages/'+NAME+'/scarpet_strfmt.sublime-color-scheme')
            with TEMPLATE_SCHEME.open('wb') as scheme_f:
                scheme_f.write(scheme_content)

        for view in views:
            view.run_command('scarpet')

    def on_load_async(self, view: sublime.View) -> None:
        view.run_command('scarpet')

    def on_modified_async(self, view: sublime.View) -> None:
        view.run_command('scarpet')

class ScarpetCommand(sublime_plugin.TextCommand):
    def run(self, edit: sublime.Edit) -> None:
        if self.view.settings().get('syntax') in SCARPET_SETTINGS.get('disabled_syntax', []):
            return
        self.create_scheme_link(current_scheme())

    def create_scheme_link(self, current_scheme: Path) -> Path:
        scheme_link = PACKAGE_SCHEME_FOLDER/current_scheme.name

        if not scheme_link.exists():
            scheme_link.symlink_to(TEMPLATE_SCHEME)
        return scheme_link
# window.run_command(
#             'edit_settings',
#             {
#                 'base_file': '/'.join(("${packages}",) + scheme_path.parts[1:]),
#                 'user_file': "${packages}/User/" + scheme_path.stem + '.sublime-color-scheme',
#                 'default': SCHEME_TEMPLATE,
#             },
#         )