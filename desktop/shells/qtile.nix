let
    shell_name = "r";
in { pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    #nativeBuildInputs = with pkgs.buildPackages; [ ruby_3_2 ];
    name = "${shell_name}";

    packages = [
        (pkgs.python3.withPackages (ps: [
            ps.qtile
            ps.pynput
        ]))
    ];
    #nativeBuildInputs = with pkgs.buildPackages; [
    #    python311
    #    python311Packages.pip
    #];
    shellHook = "
        export names=$names:qtile
    ";
}
