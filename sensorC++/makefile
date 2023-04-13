all: capteur.o application

capteur: capteur.o
	g++ -Wall -c capteur.cpp

application:capteur.o
	g++ capteur.o -o application -lwiringPi
