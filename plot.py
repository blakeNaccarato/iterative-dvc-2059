from shutil import copy


src = "in.png"
copy(src, "path/fail.png")
copy(src, "path/pass.png")
