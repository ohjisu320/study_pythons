space01="1"
space02=""
space03="2"
space04=""
space05="3"

print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))
space04=space03
space03=""
print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))

space03=space05
space05=""
print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))

space02=space01
space01=""
print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))

space01=space03
space03=""
print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))

space03=space04
print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))

space05=space02
space02=""
print("{}/{}/{}/{}/{}" .format(space01, space02, space03, space04, space05))


