To publish, run `./build.sh`, then `git push`.

Files added to `content` will not appear on the public website until the build script is used.

Python environments for each blog post should be specified by a `requirements.txt` file in that
post's subdirectory.

The `build-envs.sh` does a few things.

1. It install `jupyter` into the current environment if it is not already installed.
2. It creates a venv for for each post with a `requirements.txt` file. The venv is installed in
   the `~/venvs` directory, which is created if it does not already exist.
3. It registers a kernel with jupyter for each venv. The name of the kernel will be the same as the
   name of the subdirectory of the corresponding post.

The `jupyter: <kernel-name>` option should be set in the `yml` frontmatter of blogposts that use
python, where `<kernel-name>` is the name of the post's subdirectory.
