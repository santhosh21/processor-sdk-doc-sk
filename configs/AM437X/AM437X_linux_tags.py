# Device Family is AM437X = AM437X family
fam_name = 'AM437X'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families
project = u'Processor SDK Linux for AM437X'
html_title = 'Processor SDK Linux for AM437X Documentation'

# The master toctree document.
master_doc = 'devices/AM437X/linux/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['rtos', 'android', 'linux/index.rst', 'devices/AM437X/rtos', 'devices/AM335X', 'devices/AM64X', 'devices/AM65X', 'devices/J7', 'devices/J7200', 'devices/DRA821A']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'