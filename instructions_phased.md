GERMAN_ANKI_WORKFLOW_CONFIG (v4.0)

I am using Anki Flash Cards with the following note types:
My-German-Verb:Deutsch|English|Aussprache|Verbtyp|Valenz|Mit Präposition|Partizip II|Hilfsverb|Präsens|Präteritum|Imperativ|Beispiel|Example|Audio
My-German-Adjective:Deutsch|English|Aussprache|Deklination|Steigerung|Komparativ|Superlativ|Gegenteil|Synonym|Mit Präposition|Beispiel|Example|Audio
My-German-Adverb:Deutsch|English|Aussprache|Typ|Beispiel|Example|Audio
My-German-Noun:Deutsch|English|Aussprache|Genus|Beispiel|Example|Audio
My-German-Paradigm:Deutsch|English|Paradigm|Verwendung|Beispiel|Example
My-German-PragmaticExpression:Deutsch|English|Aussprache|Kontext|Beispiel|Example|Notiz|Audio
My-German-Conjunction:Deutsch|English|Aussprache|Typ|Funktion|Beispiel|Example|Audio

PHASE 1: CLASSIFICATION & ESSENTIALS (All Note Types)

    1. Auto-detect word type.

    2. Identify target Note Type; default to the most common usage if ambiguous.

    3. Fill Deutsch, English, Aussprache.

    5. Ignore Audio field.

PHASE 2: STRUCTURAL FIELDS (Type-Specific)

My-German-Verb {
    Valenz field: multiple (transitiv, intransitiv, reflexiv, mit Dativ, mit Genitiv, mit Präpositionalobjekt, mit Akk + Dativ).

    Mit Präposition field: multiple, follows the format of "[verb_prefix] [preposition] + [case]"; e.g. "denken an + Akk, denken über + Akk".

    Verbtyp field: schwach, stark, gemischt.
}

My-German-Adjective {
    Deklination field: schwach, stark, gemischt, nur prädikativ, nicht deklinierbar.

    Steigerung field: steigerbar, nicht steigerbar, begrenzt steigerbar.

    Gegenteil and Synonym fields: multiple values.

    Mit Präposition fields: multiple values.
}

My-German-Adverb {
    Typ field: multiple (lokaladverbien, temporaladverbien, modaladverbien, kausaladverbien, pronominaladverbien, konjunktionaladverbien, interrogativadverbien, relativadverbien, gradadverbien, negationsadverbien, fokusadverbien).
}

My-German-Noun {
    Genus field: der, die, das.
}

My-German-Paradigm {
    Paradigm field: all four cases for all genders and the plural.
}

My-German-PragmaticExpression {
    Kontext field: A short German phrase describing all the social situations or conversational functions.

    Notiz field: A free-form field in German containing usage nuances, cultural context, synonyms, or grammar notes.
}

My-German-Conjunction {
    Typ field: nebenordnende Konjunktionen, unterordnende Konjunktionen, Konjunktionaladverbien.

    Funktion field: multiple (kopulativ, disjunktiv, adversativ, kausal, konditional, konsekutiv, konzessiv, final, temporal, modal, lokal).
}

PHASE 3: BEISPIEL GENERATION (Type-Specific Rules)

Each example on a new line.

Example field is the English translation of Beispiel.

My-German-Verb {
    Generate one distinct example for every individual value listed in the Valenz field.
    
    Separately, generate one distinct example for every individual prepositional phrase listed in the Mit Präposition field.

    format:
        ([preposition] + [case]) the_example
        ([Valenz]) the_example
}

My-German-Adjective {
    Must include examples for komparativ and superlativ if available.

    Must also include examples for each Mit Präposition.

    format:
        ([Steigerungsform]) the_example
        (mit Präposition [Präposition]) the_example
}

My-German-Adverb {
    Must include an example for each Typ.
    
    format:
        ([Typ]) the_example
}

My-German-Noun {
    Must include an example for Singular form
    
    If the noun is countable add an example for Plural form.
}

My-German-Paradigm {
    one for each case.
    
    format:
        ([Kasus]) the_example
}

PHASE 4: ERROR REDUCTION MECHANISMS
Checklist verification before output:

    1. All non-Beispiel fields complete

    2. Beispiel references all required elements

    3. ALL fields for the target Note Type are present in the output.

PHASE 5: OUTPUT PROTOCOL

    1. State Target Note Type first

    2. Process fields in exact order as listed in the note types

    3. For each field, follow this exact sequence:
        a. Write the field name in plain text.
        b. On the very next line, create a code block.
        c. Place only the field's value inside this code block.
        d. Close the code block.

PHASE 6: POST-OUTPUT PROMPT

don't output a sample note.
