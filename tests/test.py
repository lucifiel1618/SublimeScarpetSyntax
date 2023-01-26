import sys
import os.path
import unittesting
import sublime

def get_current_scheme():
    return sublime.find_resources(sublime.ui_info()['color_scheme']['value'])[0]

class TestSchemeGenerated(unittesting.DeferrableTestCase):
    def setUp(self):
        self.preferences = sublime.load_settings('Preferences.sublime-settings')
        self.package_userfolder = os.path.join(sublime.packages_path(), 'User', 'Scarpet')

    def test_schemetemplate_exists(self):
        yield 10
        scheme_userfolder = os.path.join(self.package_userfolder, 'Schemes')
        template_scheme_file = os.path.join(scheme_userfolder, 'ScarpetTemplate.sublime-color-scheme')
        self.assertTrue(os.path.exists(template_scheme_file),
            'Files in {:s}: {:s}'.format(scheme_userfolder, os.listdir(scheme_userfolder)))

    def test_scheme_generated(self):
        current_scheme = get_current_scheme()
        scheme_userfolder = os.path.join(self.package_userfolder, 'Schemes')
        scheme_file = os.path.join(scheme_userfolder, os.path.basename(current_scheme))
        yield 10
        if not sys.platform.startswith('win'):
            # darwin/linux
            self.assertTrue(os.path.islink(scheme_file),
                'Files in {:s}: {:s}'.format(scheme_userfolder, os.listdir(os.path.join(sublime.packages_path(), 'User'))))
        else:
            # windows
            self.assertTrue(os.path.exists(scheme_file),
                'Files in {:s}: {:s}'.format(scheme_userfolder, os.listdir(os.path.join(sublime.packages_path(), 'User'))))

    def test_switch_scheme(self):
        for test_scheme in ('Monokai.sublime-color-scheme', 'Mariana.sublime-color-scheme'):
            if test_scheme != os.path.basename(get_current_scheme()):
                break
        self.preferences.set('color_scheme', test_scheme)
        # self.test_scheme_generated()

        current_scheme = get_current_scheme()
        scheme_userfolder = os.path.join(self.package_userfolder, 'Schemes')
        scheme_file = os.path.join(scheme_userfolder, os.path.basename(current_scheme))
        yield 10
        if not sys.platform.startswith('win'):
            # darwin/linux
            self.assertTrue(os.path.islink(scheme_file),
                'Files in {:s}: {:s}'.format(scheme_userfolder, os.listdir(scheme_userfolder)))
        else:
            # windows
            self.assertTrue(os.path.exists(scheme_file),
                'Files in {:s}: {:s}'.format(scheme_userfolder, os.listdir(scheme_userfolder)))

    def test_hexcode_realization(self):
        view = sublime.active_window().open_file('new_scarpet_file.sc') # make sure we have a window to work with
        view.set_scratch(True)
        yield lambda: not view.is_loading() or None
        view.run_command('insert', {'characters': 'format(\'biory#AAAAAAooooooo Hello\', \'#147ADF World!\')'})
        yield 100
        self.assertTrue(os.path.exists(os.path.join(self.package_userfolder, os.path.basename(get_current_scheme()))),
            'Files in {:s}: {:s}'.format(self.package_userfolder, os.listdir(self.package_userfolder)))

        with open(os.path.join(self.package_userfolder, os.path.basename(get_current_scheme()))) as of:
            colorscheme = sublime.decode_value(of.read())
        result1, result2 = False, False
        for r in colorscheme.get('rules'):
            if 'markdown' in r['scope']:
                continue
            if 'markdow' in r['scope']:
                continue
            result1 |= (r.get('foreground') == '#AAAAAA')
            result2 |= (r.get('foreground') == '#147ADF')
            if result1 and result2:
                return

        self.assertTrue(False, 'expect entries "#AAAAAA" and "#147ADF" not in rules listed below:\n{}'.format(colorscheme.get('rules')))

