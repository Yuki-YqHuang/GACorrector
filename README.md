# GACorrector

GACorrector is a Python-based program used to update reference genomes and annotations. GACorrector takes a reference genome, genome annotation, sequences of new gene models and the annotations of new gene models as input; the output is an updated reference genome and and updated genome annotation file.

## Tutorial

In Linux command line, run the following command:

    git clone https://github.com/huangyq89/GACorrector.git

enter`../GACorrector/`directory，run the following command to decompress`tools.tar`package:

    tar -xzvf tools.tar

open the directory with test files`../GACorrector/test/`, run the following command:

    python ../create_gtf.py test_sequence.fasta test_sequence_annotation.gtf processed_sequence.fasta

open the directory with test files`../GACorrector/test/`, run the following command:
    
    python ../GACorrector.py test_genome.fa test_annotation.gtf test_sequence.fasta  test_sequence_annotation.gtf output_genome.fa output_annotation.gtf processed_sequence.fasta
    
Parameters accepted are in order as follows:`reference genome to be updated`、`genome annotation to be updated`、`new gene models sequences processed by create_gtf.py`、`annotation of new gene models`、`updated reference genome`、`updated genome annotation`and`raw sequences of new gene models`。
