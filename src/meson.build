pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'flashcards')
gnome = import('gnome')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'flashcards.in',
  output: 'flashcards',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

flashcards_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'cardstack.py',
  'cardstackmodel.py'
]

install_data(flashcards_sources, install_dir: moduledir)
