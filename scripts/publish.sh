#! /bin/bash 
###########################################
# Publish to pypi
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..

rm -rf build dist
python setup.py clean sdist
## install twine first `pip install twine`
twine upload dist/*