#!/usr/bin/env python3

#############################################################
# Dieses Script überprüft, ob eine gegebene Datei existiert.#
#############################################################


def FileExists(Filename):
  try:
    f = open(Filename, "r")
    f.close()
    return True
  except IsADirectoryError:
    return True
  except PermissionError:
    return False
  except FileNotFoundError:
    return False

def help():
  print(str(sys.argv[0]) + " [Dateiname] überprüft, ob eine")
  print("gegebene Datei vorhanden ist.")
  sys.exit(0)


if __name__ == '__main__':
  import sys

  if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
      help()
    if FileExists(sys.argv[1]):
      print("Die Datei oder der Ordner existiert.")
    elif not FileExists(sys.argv[1]):
      print("Die Datei oder der Ordner existiert nicht.")
  elif len(sys.argv) == 1:
    help()
  elif len(sys.argv) > 2:
    print("Nur ein Argument erwartet.")
