#include <stdio.h>
#include <stdbool.h>

/*
Idées :
Scale de départ donné avec les mesures
-Lire la scale + profondeur dans un fichier txt ou autre
ATTENTION On a pas forcément tous les points de la grille dans le fichier, et ils ne sont pas forcément dans le bon ordre
Fichier:
1   width   heigh   maxDepth
2   coord_i coord_j profond_z (en m)
...

-indiquer le Nord
-utiliser SDL pour la 2D?

-gradient de couleur : que faire entre les points? interpolation couleur ou interpolation profondeur

-Scale pouvant être augmenté ou diminué par interpolations
    => créer une autre map utilisant une autre scale
*/

/*=========== Global ===========*/

Map carte;
Scale echelle = {50.0 , 50.0, 15.0,  200, 300, 500};

/*=========== Structures ===========*/
typedef struct {
    float x;
    float y;
} Point;

typedef struct{
    float width;//en m
    float height;//en m
    float maxDepth;//en m
    int wStep;
    int hStep;
    int dStep;

} Scale;

typedef struct {
    float** array;
} Map;

/*=========== Fonctions ===========*/

bool initMap(Map* map, Scale* scale){
    
    map->array= malloc(sizeof(float)*scale->hStep * scale->wStep);
    if (map->array == NULL){return false;}

    for (int i = 0; i< scale -> hStep ; i++){
        for (int j=0; j< scale -> wStep ; j++){
            map->array[i][j]= 0.0;
        }
    }

    return true;
}

bool readData(const char *nomFichier) {

    FILE *fichier = fopen(nomFichier, "r");

    if (fichier == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return false;
    }

    char ligne[256]; 
    int cpt =0;
    int ind_i;
    int ind_j;

    while (fgets(ligne, sizeof(ligne), fichier) != NULL) {
        printf("Line %d : %s", cpt++ ,ligne);
        //TODO
        //enregistrer le point dans la carte (il faut trouver le point le plus proche des coordonnées lues et assigner la profondeur)
    }

    fclose(fichier);
    return false;
}

void closestInGrid(float nb_i, float nb_j, int* ind_i, int* ind_j){
    //TODO
    //tester les 4 points autour
    return;
}

Point getCoords(Scale* scale, int i, int j){
    Point pt = {i*scale->height/scale->hStep , j*scale->width/scale->wStep};
    return pt;
}

bool saveMap(Map* map, Scale* scale, const char *nomFichier){
    FILE *fichier = fopen(nomFichier, "w");

    if (fichier == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return false;
    }

    for (int i = 0; i < scale->hStep; i++) {
        for (int j = 0; j < scale->wStep; j++) {
            fprintf(fichier, "%.2f", map->array[i][j]);
            if (j < scale->wStep - 1) {fprintf(fichier, "\t");}
        }

        fprintf(fichier, "\n");  
    }

    fclose(fichier);
    return true;
}



bool destroyAll(Map* map){
    free(map->array);
    return true;
}

int main(int argc, char* argv[]){

    if (!initMap(&carte, &echelle)){
        printf("Merde!\n");
        return 1;
    };
    


    return 0;
}