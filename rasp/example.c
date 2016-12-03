#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "SkyeTekAPI.h"
#include "SkyeTekProtocol.h"

int main(int argc, char* argv[])
{
	LPSKYETEK_DEVICE *devices = NULL;
	LPSKYETEK_READER *readers = NULL;
	LPSKYETEK_TAG *tags = NULL;
	SKYETEK_STATUS status;
	unsigned short count = 0;
	int numDevices = 0;
	int numReaders = 0;
	const int delay = 400000;  	//wait at least 400ms after closing the interface before re-opening (USB enumeration)
	const int tests = 3; 		//number of open/close tests to perform
	const int iterations = 10; 	//number of select tag operations to perform for each test
	int failures = 0;
	int total = 0;

    printf("Appareils trouvés %d\n", SkyeTek_DiscoverDevices(&devices));
    numDevices = SkyeTek_DiscoverDevices(&devices);
    printf("Lecteurs trouvés : %d\n", SkyeTek_DiscoverReaders(devices,numDevices,&readers));
    printf("Reader Found: %s-%s-%s\n", readers[0]->manufacturer, readers[0]->model, readers[0]->firmware);

    for(int k = 0; k < iterations; k++)
    {
        printf("\tIteration = %d\n",k);
        status = SkyeTek_GetTags(readers[0], AUTO_DETECT, &tags, &count);
        if(status == SKYETEK_SUCCESS)
        {
            if(count == 0)
            {
                printf("\t\tNo tags found\n");
            }
            else
            {
                for(int j = 0; j < count; j++)
                {
                    printf("\t\tTag Found: %s-%s\n", SkyeTek_GetTagTypeNameFromType(tags[j]->type), tags[j]->friendly);
                    printf("\t\tTruc bizarre encore : %s, de taille %d\n", tags[j]->friendly, sizeof(tags[j]->friendly));
                }
            }
        }
        else
        {
            printf("ERROR: GetTags failed\n");
        }
    }
    SkyeTek_FreeTags(readers[0],tags,count);
}
