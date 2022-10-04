bilboquets = int(input('Nombre de Bilboquets en stock?'))
lampes = int(input('Nombre de Lampes en stock?'))
boules_i = int(input('Nombre de boules initiales?'))
pieds_i = int(input('Nombre de pieds initials'))
socles_i = int(input('Nombre de socles initials'))
abat_i = int(input("Nombre d'abats jours initials"))

bilboquets_demandés = int(input('Combien de bilboquets sont demandés'))
lampes_demandées = int(input('Combien de lampes sont demandées'))

bilboquets_final = bilboquets_demandés - bilboquets
lampes_final = lampes_demandées - lampes

print('Le nombre de bilboquets requis est de :', bilboquets_final)
print('Le nombre de lampes requis est de :', lampes_final )

# Calcul par stock déjà présent dans l'entreprise

produit_total = bilboquets_final + lampes_final

boules_f = produit_total - boules_i
print('il faut ', boules_f, ' boules')

pieds_f = produit_total - pieds_i
print('il faut ', pieds_f, ' pieds')

socles_f = lampes_final - socles_i
print('il faut', socles_f, ' socles')

abat_f = lampes_final - abat_i
print('il faut', abat_f, ' abats')


prix_total = 0

prix_b = 5.25
prix_p = 3.10
prix_s = 5.20
prix_a = 16

prix_total = prix_a * lampes_final + prix_p * produit_total + prix_s * lampes_final + prix_b * produit_total

print('prix final :', prix_total)

vente_bilboquets = float(input("Prix d'un bilboquet ?"))
vente_lampes = float(input("Prix d'une lampe? "))

vente_bilboquets_t = bilboquets_final * vente_bilboquets
vente_lampes_t = lampes_final * vente_lampes
vente_t = vente_bilboquets_t + vente_lampes_t


print('Prix de vente des 2 : ', vente_t)

#Le salaire de l'artisan est de 2000€ par mois

rep = input("Voulez vous le profit avec ou sans le salaire de l'artisan?")
if rep == "avec" :
    profit = vente_t - prix_total - 2000
    print('Le profit est de :', profit, " en prenant compte du salaire de l'artisan")
else :
    profit = vente_t - prix_total
    print('Le profit est de :', profit, " sans prendre en compte le salaire de l'artisan")