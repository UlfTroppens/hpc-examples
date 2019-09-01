#include <mpi.h>
#include <stdio.h>
#include <unistd.h>

int
main(int argc, char *argv[])
{
    int mpi_rank, mpi_size;
    char hostname[256];

    // Initialize MPI execution environment
    MPI_Init(&argc, &argv);

    // Get MPI size and rank
    MPI_Comm_size(MPI_COMM_WORLD, &mpi_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &mpi_rank);

    // Get my hostname
    gethostname(hostname, sizeof(hostname));

    // Report my execution context
    printf("My size is %d. My rank is %d. I am running on %s.\n", mpi_size, mpi_rank, hostname );

    // Terminate MPI execution environment
    MPI_Finalize();

    // Exit without error
    return 0;
}
