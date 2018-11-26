from enum import Enum


class Parameter(Enum):
    EMBEDDINGS = 'embeddings'
    HIDDEN_SIZE = 'hidden_size'
    USE_CRF = 'use_crf'
    USE_RNN = 'use_rnn'
    RNN_LAYERS = 'rnn_layers'
    USE_DROPOUT = 'use_dropout'
    USE_WORD_DROPOUT = 'use_word_dropout'
    USE_LOCKED_DROPOUT = 'use_locked_dropout'
    LEARNING_RATE = 'learning_rate'
    MINI_BATCH_SIZE = 'mini_batch_size'
    ANNEAL_FACTOR = 'anneal_factor'
    ANNEAL_WITH_RESTARTS = 'anneal_with_restarts'
    PATIENCE = 'patience'
    REPROJECT_WORDS = 'reproject_words'
    REPROJECT_WORD_DIMENSION = 'reproject_words_dimension'
    BIDIRECTIONAL = 'bidirectional'


TRAINING_PARAMETERS = [
    Parameter.LEARNING_RATE.value,
    Parameter.MINI_BATCH_SIZE.value,
    Parameter.ANNEAL_FACTOR.value,
    Parameter.PATIENCE.value,
    Parameter.ANNEAL_WITH_RESTARTS.value
]
SEQUENCE_TAGGER_PARAMETERS = [
    Parameter.EMBEDDINGS.value,
    Parameter.HIDDEN_SIZE.value,
    Parameter.RNN_LAYERS.value,
    Parameter.USE_CRF.value,
    Parameter.USE_RNN.value,
    Parameter.USE_DROPOUT.value,
    Parameter.USE_LOCKED_DROPOUT.value,
    Parameter.USE_WORD_DROPOUT.value
]
DOCUMENT_EMBEDDING_PARAMETERS = [
    Parameter.EMBEDDINGS.value,
    Parameter.HIDDEN_SIZE.value,
    Parameter.RNN_LAYERS.value,
    Parameter.REPROJECT_WORDS.value,
    Parameter.REPROJECT_WORD_DIMENSION.value,
    Parameter.BIDIRECTIONAL.value,
    Parameter.USE_LOCKED_DROPOUT.value,
    Parameter.USE_WORD_DROPOUT.value
]
