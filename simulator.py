import os


def read_repo_db(file_name):
    db = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    key, value = parts
                    db[key] = set(value.split())
                else:
                    raise ValueError(f"Incorrect format on line: {line}")
    return db


def read_pkgs_db(file_name):
    db = set()
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                db.add(line.strip())
    return db


def install(pkg_name, repo_db, pkgs_db):
    if pkg_name in pkgs_db:
        print(f"{pkg_name} is already installed.")
        return

    to_install = [pkg_name]

    while to_install:
        curr_pkg = to_install.pop()

        if curr_pkg not in pkgs_db:
            print(f"Installing {curr_pkg}")
            pkgs_db.add(curr_pkg)

            if curr_pkg in repo_db:
                for pkg in repo_db[curr_pkg]:
                    if pkg not in pkgs_db and pkg not in to_install:
                        to_install.append(pkg)


def uninstall(pkg_name, repo_db, pkgs_db):
    if pkg_name not in pkgs_db:
        print(f"{pkg_name} is not installed.")
        return

    to_uninstall = [pkg_name]
    deleted = []

    while to_uninstall:
        curr_pkg = to_uninstall.pop()

        for pkg, deps in repo_db.items():
            if curr_pkg in deps and pkg in pkgs_db:
                to_uninstall.append(pkg)

        print(f"Uninstalling {curr_pkg}")
        pkgs_db.remove(curr_pkg)
        deleted.append(curr_pkg)


def list_installed(db):
    print("Installed packages:")
    for pkg in sorted(db):
        print(f"{pkg}")


def write_pkgs(db):
    with open("pkgs.db", "w") as f:
        for pkg in db:
            f.write(f"{pkg}\n")


# ----------------main-----------------
repo_db = read_repo_db("repo.db")
pkgs_db = read_pkgs_db("pkgs.db")

action = input("pkg ")
command, *pkg_name = action.split()

if command == "install" and pkg_name:
    install(pkg_name[0], repo_db, pkgs_db)
elif command == "uninstall" and pkg_name:
    uninstall(pkg_name[0], repo_db, pkgs_db)
elif command == "list":
    list_installed(pkgs_db)
else:
    print("Invalid Command")
    exit(0)

write_pkgs(pkgs_db)
