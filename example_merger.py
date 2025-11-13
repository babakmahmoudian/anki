""" This module reads the values of the separate fields 'beispieler' and
    'example' and merges them into a single 'beispieler' field. """


import pandas as pd

df = pd.read_csv('./Selected Notes.txt', sep='\t', skiprows=2, header=None)


def merger(df):
    """ Receives the notes as a dataframe and merges the two fields. """

    def divide_and_merge(row):
        """ Takes a single note in terms of the two fields of "Beispieler" and
            "Example", splits the value of each field by linebreaks,
            and merges them into a single field."""

        print(f"processing {row.iloc[0]} ...", end='')

        linebreak = '<br>'
        beispiels = row.iloc[-2].split(linebreak)
        examples = row.iloc[-1].split(linebreak)

        merged = []
        for b, e in zip(beispiels, examples):
            merged.append(f"<b>{b}</b>{linebreak}{e}")

        print(" Done.", flush=True)
        return '<br>'.join(merged)

    df['res'] = (df.drop(df.columns[-2:], axis=1)
                 .iloc[:, [0, -2, -1]]
                 .apply(divide_and_merge, axis=1))

    return df


df_red = merger(df)
df_red.to_csv('./Notes Merged.csv', sep='\t', index=False, header=False)

print(
    f"Total of {len(df_red)} notes processed and saved to './Notes Merged.csv'.")
