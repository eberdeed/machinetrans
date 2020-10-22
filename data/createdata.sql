CREATE TYPE word_var AS ENUM ('noun', 'adjective', 'verb', 
    'adverb', 'interjection', 'pronoun', 
    'article', 'preposition', 'symbol', 'conjunction', 
    'interrogative');
CREATE TYPE noun_var AS ENUM ('abstract', 'proper', 'concrete', 
    'collective', 'compound');
CREATE TYPE verb_var AS ENUM ('participle',  'modal', 'helper', 'regular', 'auxiliary');
CREATE TYPE adj_var AS ENUM ('descriptive', 'comparative', 'superlative');
CREATE TYPE adv_var AS ENUM ('manner', 'place', 'time', 'degree');
CREATE TYPE pron_var AS ENUM ('personal', 'demonstrative', 'posessive', 
    'interrogative', 'reflexive', 'reciprocal', 'indefinite', 
    'relative');
CREATE TYPE prtcpl_var AS ENUM ('present active', 'present passive', 
    'past active', 'past passive', 'verbal adverb');
CREATE TYPE artcl_var AS ENUM ('definite', 'indefinite');
CREATE TYPE prep_var AS ENUM ('place', 'time');
CREATE TYPE conj_var AS ENUM ('coordinating', 'subordinating');
CREATE TYPE symb_var AS ENUM ('glyph', 'number');
CREATE TYPE intrgs_var AS ENUM ('person', 'place', 'time', 'method', 'reason', 'ownership');
CREATE TYPE tense_var AS ENUM ('imperative', 'simple present', 'simple past', 
    'perfect simple past', 'perfect continuous past', 
    'continuous past', 'continuous present', 'perfect simple present', 
    'perfect continous present', 'simple future', 'continuous future', 
    'perfect simple future', 'perfect continuous future');
CREATE TYPE pstat_var AS ENUM ('subject', 'object');
CREATE TYPE ntype_var AS ENUM ('location', 'thing');
CREATE TYPE prsn_var AS ENUM ('first', 'second', 'third', 'plural first', 'plural second', 'plural third');
CREATE TYPE actvt_var AS ENUM ('motion', 'contemplative');
CREATE TYPE case_var AS ENUM ('nominative', 'accusative', 'genitive', 'dative', 'instrumental', 'prepositional');
CREATE TYPE gender_var AS ENUM ('masculine', 'feminine', 'nueter');
CREATE TYPE number_var as ENUM ('singular', 'plural');
CREATE TABLE nouns( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety noun_var DEFAULT 'concrete', 
    gender gender_var DEFAULT 'masculine',
    type ntype_var DEFAULT 'thing',
    singplur number_var DEFAULT 'singular',
    declension text DEFAULT '',
    wordcase case_var DEFAULT 'nominative'
    );
CREATE TABLE interjections( 
    name text DEFAULT '', 
    runame text DEFAULT ''
    );
CREATE TABLE verbs( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety verb_var DEFAULT 'regular', 
    tense tense_var DEFAULT 'simple present', 
    person prsn_var DEFAULT 'third', 
    conjugationru text DEFAULT '',
    conjugation text DEFAULT ''
    );
CREATE TABLE adjectives( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety adj_var DEFAULT 'descriptive', 
    gender gender_var DEFAULT 'masculine',
    singplur number_var DEFAULT 'singular',
    declension text DEFAULT '',
    wordcase case_var DEFAULT 'nominative'
    );
CREATE TABLE shortadjectives( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety adj_var DEFAULT 'descriptive', 
    gender gender_var DEFAULT 'masculine',
    singplur number_var DEFAULT 'singular'
    );
CREATE TABLE adverbs( 
    name text DEFAULT ' ', 
    runame text DEFAULT '',
    variety adv_var DEFAULT 'manner' 
    );
CREATE TABLE pronouns( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety pron_var DEFAULT 'personal',
    gender gender_var DEFAULT 'masculine',
    status pstat_var DEFAULT 'subject', 
    person prsn_var DEFAULT 'first',
    declension text DEFAULT '',
    wordcase case_var DEFAULT 'nominative'
    );
CREATE TABLE participles( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety prtcpl_var DEFAULT 'past passive' ,
    gender gender_var DEFAULT 'masculine',
    singplur number_var DEFAULT 'singular',
    declension text DEFAULT '',
    wordcase case_var DEFAULT 'nominative'
    );
CREATE TABLE articles( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety artcl_var DEFAULT 'definite', 
    gender gender_var DEFAULT 'masculine',
    singplur number_var DEFAULT 'singular',
    declension text DEFAULT '',
    wordcase case_var DEFAULT 'nominative'
    );
CREATE TABLE prepositions( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety prep_var DEFAULT 'place' 
    );
CREATE TABLE conjunctions( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety conj_var DEFAULT 'coordinating' 
    );
CREATE TABLE symbols( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety symb_var DEFAULT 'number' 
    );
CREATE TABLE interrogatives( 
    name text DEFAULT '', 
    runame text DEFAULT '',
    variety intrgs_var DEFAULT 'person',
    gender gender_var DEFAULT 'masculine',
    status pstat_var DEFAULT 'subject',
    singplur number_var DEFAULT 'singular',
    declension text DEFAULT '',
    wordcase case_var DEFAULT 'nominative'
    );