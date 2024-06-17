#!/bin/sh

if ! command -v git-lfs &> /dev/null; then
	echo "Install git-lfs to get the tarball"
	exit
fi

git-lfs fetch
git-lfs checkout

if [ ! -d "raw" ]; then
	mkdir "raw" -pv
fi

echo "Extracting raw.tar.gz:\n"
if command -v pv &> /dev/null; then
	pv raw.tar.gz | tar xz --directory=raw
else
	"To display progress, please install 'pv'"
	tar xf raw.tar.gz --directory=raw
fi
echo "Done"
