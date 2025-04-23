import PySimpleGUI as sg
import pandas as pd
import os

sg.theme('LightBlue2')

layout = [
    [sg.Text('Selecione o Ficheiro WZPRE (Ficheiro 1):')],
    [sg.Input(key='-WZPRE-'), sg.FileBrowse(file_types=[("Excel Files", "*.xlsx"), ("CSV Files", "*.csv")])],

    [sg.Text('Selecione o Ficheiro de Referência (Ficheiro 2):')],
    [sg.Input(key='-REF-'), sg.FileBrowse(file_types=[("Excel Files", "*.xlsx"), ("CSV Files", "*.csv")])],

    [sg.Text('Formato de saída:'), 
     sg.Radio('Excel (.xlsx)', 'FORMAT', default=True, key='-EXCEL-'),
     sg.Radio('CSV (.csv)', 'FORMAT', key='-CSV-')],

    [sg.Button('Executar', button_color=('white', '#28a745'), font=('Helvetica', 12, 'bold'), size=(12, 1)), 
     sg.Button('Limpar', button_color=('white', 'orange')), 
     sg.Button('Ajuda', button_color=('white', 'blue'))],

    [sg.Text('Progresso do Processamento:')],
    [sg.ProgressBar(100, orientation='h', size=(50, 20), key='-PROGRESS-'),
     sg.Text('0%', key='-PERCENT-', size=(5, 1))],

    [sg.Text('', key='-STATUS-', size=(70,2))],
    [sg.Text('Prévia do Resultado:'), sg.Multiline('', key='-PREVIEW-', size=(100, 15), disabled=True)]
]

window = sg.Window('Filtrador de Referências - Versão Final', layout)

def encontrar_coluna_referencia(df):
    for col in df.columns:
        if 'referencia' in str(col).lower():
            return col
    return None

def atualizar_progresso(percent):
    window['-PROGRESS-'].update_bar(percent)
    window['-PERCENT-'].update(f'{percent}%')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'Limpar':
        window['-WZPRE-'].update('')
        window['-REF-'].update('')
        window['-STATUS-'].update('')
        window['-PREVIEW-'].update('')
        window['-EXCEL-'].update(True)
        window['-CSV-'].update(False)
        atualizar_progresso(0)

    elif event == 'Ajuda':
        sg.popup('Este programa filtra o Ficheiro 1 (WZPRE) com base nas referências presentes no Ficheiro 2.\n\n'
                 '1. Selecione os dois ficheiros.\n'
                 '2. Escolha o formato de saída.\n'
                 '3. Clique em Executar para gerar o ficheiro filtrado.\n'
                 'Apenas as linhas cujas referências estiverem em ambos os ficheiros serão mantidas.')

    elif event == 'Executar':
        try:
            atualizar_progresso(0)
            wzpre_path = values['-WZPRE-']
            ref_path = values['-REF-']

            if wzpre_path.endswith('.csv'):
                df1 = pd.read_csv(wzpre_path, sep=';', dtype=str, encoding='utf-8')
            else:
                df1 = pd.read_excel(wzpre_path, dtype=str)

            df1 = df1.astype(str).apply(lambda col: col.str.strip())
            atualizar_progresso(25)

            if ref_path.endswith('.csv'):
                df2 = pd.read_csv(ref_path, dtype=str, encoding='utf-8')
            else:
                df2 = pd.read_excel(ref_path, dtype=str)

            df2 = df2.astype(str).apply(lambda col: col.str.strip())
            atualizar_progresso(50)

            col_ref_1 = encontrar_coluna_referencia(df1)
            col_ref_2 = encontrar_coluna_referencia(df2)

            if not col_ref_1 or not col_ref_2:
                window['-STATUS-'].update('Nenhuma coluna com "referencia" encontrada.', text_color='red')
                continue

            total_antes = len(df1)
            df_filtrado = df1[df1[col_ref_1].isin(df2[col_ref_2])]
            total_depois = len(df_filtrado)
            removidos = total_antes - total_depois
            atualizar_progresso(75)

            base_dir = os.path.dirname(wzpre_path)
            output_path = os.path.join(base_dir, 'resultado_filtrado')

            if values['-CSV-']:
                output_path += '.csv'
                df_filtrado.to_csv(output_path, index=False, sep=';', encoding='utf-8')
            else:
                output_path += '.xlsx'
                df_filtrado.to_excel(output_path, index=False)
            atualizar_progresso(100)

            preview_text = df_filtrado.head(20).to_string(index=False)
            window['-PREVIEW-'].update(preview_text)

            status_msg = f'{total_depois} linha(s) mantida(s), {removidos} excluída(s).\nArquivo salvo em:\n{output_path}'
            window['-STATUS-'].update(status_msg, text_color='green')

        except Exception as e:
            window['-STATUS-'].update(f'Erro: {str(e)}', text_color='red')
            atualizar_progresso(0)

window.close()
