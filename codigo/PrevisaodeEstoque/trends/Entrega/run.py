from trends import trends
import csv

trend = trends()

terms = [
    "Cansaco",
	"Dor atras dos olhos",
	"Dor de cabeca",
	"Dor nas articulacoes",
	"Dor muscular",
	"Dor nos ossos",
	"Febre",
	"Manchas vermelhas pelo corpo",
	"Moleza",
	"Nausea",
	"Perda de paladar e apetite",
	"Tontura",
	"Vomito",
	"Aumento do tamanho do baco",
	"Aumento do tamanho do figado",
	"Diarreia",
	"Dor no corpo",
	"Fadiga",
	"Irritacao sobre a pele",
	"Mal estar",
	"Surgimento de nodulos",
	"Dor abdominal",
	"sangue nas fezes",
	"Tosse",
	"Arritmia",
	"falta de apetite",
	"machas rosadas no tronco",
	"Dor lombar",
	"Hemorragias",
	"Hipotensao",
	"Rubor facial",
	"Aparecimento de feridas na pele",
	"crescimento progressivo das feridas",
	"anemia",
	"indisposicao",
	"Palidez",
	"perda de peso",
	"Ictericia",
	"insuficiencia hepatica",
	"insuficiencia renal",
	"insuficiencia respiratoria",
	"Calafrios",
	"convulsoes",
	"desorientacao",
	"confusao mental",
	"Dificuldade de concentracao",
	"Fotossensibilidade",
	"Pescoco rigido",
	"sonolencia",
	"Espasmos musculares",
	"Hipertensao",
	"rigidez no maxilar",
	"Rigidez nos musculos de pescoco e nuca",
	"Rigidez nos musculos do abdomen",
	"Sudorese"
]

half = int(len(terms)/2)
terms0 = terms[0:half]
terms1 = terms[half:int(len(terms))]

print(trend.get_trends_safe(terms0))
print(trend.get_trends_safe(terms1))
