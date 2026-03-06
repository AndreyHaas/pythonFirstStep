plastik_flaschen_stk = int(input('Geben Sie Anzahl der Plastikflaschen ein: '))
glas_flaschen_stk = int(input('Geben Sie Anzahl der Glasflaschen ein: '))

pfand_pf = plastik_flaschen_stk * 0.25
pfand_gf = glas_flaschen_stk * 0.15

pfand_satz_gesamt = pfand_pf + pfand_gf
print(f'Gesamtpfand: {pfand_satz_gesamt:.2f} €')

if pfand_satz_gesamt < 1:
    print('Sie haben nur wenige Flaschen abgegeben.')
elif pfand_satz_gesamt <= 5:
    print('Eine gute Menge an Flaschen zurückgegeben!')
else:
    print('Wow, das sind viele Flaschen!')