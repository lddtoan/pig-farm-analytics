import locale
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pathlib import Path


DATA = 'data/mycotoxins-perturbation.csv'
SIM = 'simulations'

OUTPUT = 'output'
OUTPUT_DATA = 'output/data'
OUTPUT_SIM = 'output/sim'


def _setup():
    locale.setlocale(locale.LC_ALL, '')
    Path(OUTPUT_DATA).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_SIM).mkdir(parents=True, exist_ok=True)


def _plot_data(id_rep1: list, id_rep2: list, data_rep1: pd.DataFrame, data_rep2: pd.DataFrame, prefix=''):
    '''
    Columns:
    - Ordre: id
    - day: experiment day n.o.
    - DFI: daily feed intake
    '''
    for id in id_rep1:
        data_rep1[data_rep1['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).reset_index(drop=True).plot.line()
        plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep1_{id}_dfi.png'))
        plt.clf()
        data_rep1[data_rep1['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).cumsum().reset_index(drop=True).plot.line()
        plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep1_{id}_cfi.png'))
        plt.clf()

    for id in id_rep2:
        data_rep2[data_rep2['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).reset_index(drop=True).plot.line()
        plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep2_{id}_dfi.png'))
        plt.clf()
        data_rep2[data_rep2['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).cumsum().reset_index(drop=True).plot.line()
        plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep2_{id}_cfi.png'))
        plt.clf()


    for id in id_rep1:
        data_rep1[data_rep1['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).reset_index(drop=True).plot.line()
    plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep1_dfi.png'))
    plt.clf()
    for id in id_rep1:
        data_rep1[data_rep1['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).cumsum().reset_index(drop=True).plot.line()
    plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep1_cfi.png'))
    plt.clf()

    for id in id_rep2:
        data_rep2[data_rep2['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).reset_index(drop=True).plot.line()
    plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep2_dfi.png'))
    plt.clf()
    for id in id_rep2:
        data_rep2[data_rep2['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).cumsum().reset_index(drop=True).plot.line()
    plt.savefig(os.path.join(OUTPUT_DATA, f'{prefix}_data_rep2_cfi.png'))
    plt.clf()


def _plot_sim(data: list, prefix=''):
    for index, value in enumerate(data):
        value['pig.dfi'].plot.line()
        plt.savefig(os.path.join(OUTPUT_SIM, f'{prefix}_sim_{index}_dfi.png'))
        plt.clf()
        value['pig.cfi'].plot.line()
        plt.savefig(os.path.join(OUTPUT_SIM, f'{prefix}_sim_{index}_cfi.png'))
        plt.clf()
    for index, value in enumerate(data):
        value['pig.dfi'].plot.line()
    plt.savefig(os.path.join(OUTPUT_SIM, f'{prefix}_sim_dfi.png'))
    plt.clf()
    for index, value in enumerate(data):
        value['pig.cfi'].plot.line()
    plt.savefig(os.path.join(OUTPUT_SIM, f'{prefix}_sim_cfi.png'))
    plt.clf()


def _parse_data():
    '''
    Columns:
    - lot: experiment type
    - rep: experiment replicate id
    '''
    data = pd.read_csv(DATA)

    cc_data = data[data['lot'] == 'CC']
    dc_data = data[data['lot'] == 'DC']
    cd_data = data[data['lot'] == 'CD']
    dd_data = data[data['lot'] == 'DD']

    cc_id_rep1 = [10, 12, 26, 27, 35, 54, 55, 57, 63, 68, 71, 80, 84, 85, 90, 96, 105, 115]
    cc_id_rep2 = [2, 9, 15, 18, 21, 32, 45, 48, 59, 60, 61, 63, 67, 81, 82, 94, 95, 97, 101, 115, 120]
    cc_data_rep1 = cc_data[cc_data['rep'] == 1]
    cc_data_rep2 = cc_data[cc_data['rep'] == 2]

    dc_id_rep1 = [15, 24, 29, 31, 37, 39, 49, 50, 52, 67, 69, 79, 88, 97, 102, 108, 111, 112]
    dc_id_rep2 = [5, 8, 17, 24, 27, 31, 34, 49, 54, 58, 68, 72, 76, 92, 99, 100, 102, 106, 107, 109, 117]
    dc_data_rep1 = dc_data[dc_data['rep'] == 1]
    dc_data_rep2 = dc_data[dc_data['rep'] == 2]

    cd_id_rep1 = [5, 17, 18, 21, 23, 30, 40, 44, 62, 70, 86, 92, 98, 100, 109, 120]
    cd_id_rep2 = [7, 11, 13, 16, 20, 23, 35, 37, 43, 47, 55, 56, 65, 71, 73, 77, 79, 86, 87, 89, 112, 116]
    cd_data_rep1 = cd_data[cd_data['rep'] == 1]
    cd_data_rep2 = cd_data[cd_data['rep'] == 2]

    dd_id_rep1 = [8, 13, 19, 28, 47, 53, 56, 65, 66, 73, 76, 77, 78, 81, 82, 99, 107, 110]
    dd_id_rep2 = [10, 14, 22, 28, 41, 50, 51, 62, 64, 66, 85, 90, 93, 96, 98, 105, 108, 110, 113, 114, 119]
    dd_data_rep1 = dd_data[dd_data['rep'] == 1]
    dd_data_rep2 = dd_data[dd_data['rep'] == 2]

    _plot_data(cc_id_rep1, cc_id_rep2, cc_data_rep1, cc_data_rep2, 'cc')
    _plot_data(dc_id_rep1, dc_id_rep2, dc_data_rep1, dc_data_rep2, 'dc')
    _plot_data(cd_id_rep1, cd_id_rep2, cd_data_rep1, cd_data_rep2, 'cd')
    _plot_data(dd_id_rep1, dd_id_rep2, dd_data_rep1, dd_data_rep2, 'dd')


def _parse_sim():
    normal_data = []
    cc_data = []
    dc_data = []
    cd_data = []
    dd_data = []
    transmit_data = []
    multi_data = []

    for i in range(20):
        normal_data.append(pd.read_csv(os.path.join(SIM, 'normal', f'{i}.csv')))
        cc_data.append(pd.read_csv(os.path.join(SIM, 'cc', f'{i}.csv')))
        dc_data.append(pd.read_csv(os.path.join(SIM, 'dc', f'{i}.csv')))
        cd_data.append(pd.read_csv(os.path.join(SIM, 'cd', f'{i}.csv')))
        dd_data.append(pd.read_csv(os.path.join(SIM, 'dd', f'{i}.csv')))
        transmit_data.append(pd.read_csv(os.path.join(SIM, 'transmit', f'{i}.csv')))
        multi_data.append(pd.read_csv(os.path.join(SIM, 'multi', f'{i}.csv')))

    _plot_sim(normal_data, 'normal')
    _plot_sim(cc_data, 'cc')
    _plot_sim(dc_data, 'dc')
    _plot_sim(cd_data, 'cd')
    _plot_sim(dd_data, 'dd')
    _plot_sim(transmit_data, 'transmit')
    _plot_sim(multi_data, 'multi')


def _get_parse_data(id_rep1: list, id_rep2: list, data_rep1: pd.DataFrame, data_rep2: pd.DataFrame):
    rep1 = []
    rep2 = []
    for id in id_rep1:
        rep1.append(data_rep1[data_rep1['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).reset_index(drop=True))
    for id in id_rep2:
        rep2.append(data_rep2[data_rep2['Ordre'] == id].sort_values('day')['DFI'].apply(lambda x: locale.atof(x) if x != '.' else 0).reset_index(drop=True))
    return rep1, rep2


def _aggregate_corr(data_rep1: list, data_rep2: list, sim: list, prefix='', type=''):
    corr1 = []
    corr2 = []
    for i in range(min(len(data_rep1), len(sim))):
        corr1.append(pd.DataFrame({'data': data_rep1[i], 'sim': sim[i]}).corr()['sim']['data'])
    for i in range(min(len(data_rep2), len(sim))):
        corr2.append(pd.DataFrame({'data': data_rep2[i], 'sim': sim[i]}).corr()['sim']['data'])
    pd.DataFrame(corr1).plot.bar()
    plt.savefig(os.path.join(OUTPUT, f'{prefix}_corr1_{type.lower()}.png'))
    plt.clf()
    pd.DataFrame(corr2).plot.bar()
    plt.savefig(os.path.join(OUTPUT, f'{prefix}_corr2_{type.lower()}.png'))
    plt.clf()
    print(f'Avg {type} {prefix.upper()} Correlation Rep 1: {sum(corr1) / len(corr1)}')
    print(f'Avg {type} {prefix.upper()} Correlation Rep 2: {sum(corr2) / len(corr2)}')
    print(f'Avg {type} {prefix.upper()} Correlation Total: {(sum(corr1) / len(corr1) + sum(corr2) / len(corr2)) / 2}')


def _diff_cfi(cfi: pd.DataFrame):
    x = np.arange(0, len(cfi))
    m, c = np.polyfit(x, cfi, 1)
    target = pd.Series(m * x + c)
    return cfi - target


def _calc_corr():
    data = pd.read_csv(DATA)

    cc_data = data[data['lot'] == 'CC']
    dc_data = data[data['lot'] == 'DC']
    cd_data = data[data['lot'] == 'CD']
    dd_data = data[data['lot'] == 'DD']

    cc_id_rep1 = [10, 12, 26, 27, 35, 54, 55, 57, 63, 68, 71, 80, 84, 85, 90, 96, 105, 115]
    cc_id_rep2 = [2, 9, 15, 18, 21, 32, 45, 48, 59, 60, 61, 63, 67, 81, 82, 94, 95, 97, 101, 115, 120]
    cc_data_rep1 = cc_data[cc_data['rep'] == 1]
    cc_data_rep2 = cc_data[cc_data['rep'] == 2]
    cc_data_rep1, cc_data_rep2 = _get_parse_data(cc_id_rep1, cc_id_rep2, cc_data_rep1, cc_data_rep2)
    
    dc_id_rep1 = [15, 24, 29, 31, 37, 39, 49, 50, 52, 67, 69, 79, 88, 97, 102, 108, 111, 112]
    dc_id_rep2 = [5, 8, 17, 24, 27, 31, 34, 49, 54, 58, 68, 72, 76, 92, 99, 100, 102, 106, 107, 109, 117]
    dc_data_rep1 = dc_data[dc_data['rep'] == 1]
    dc_data_rep2 = dc_data[dc_data['rep'] == 2]
    dc_data_rep1, dc_data_rep2 = _get_parse_data(dc_id_rep1, dc_id_rep2, dc_data_rep1, dc_data_rep2)

    cd_id_rep1 = [5, 17, 18, 21, 23, 30, 40, 44, 62, 70, 86, 92, 98, 100, 109, 120]
    cd_id_rep2 = [7, 11, 13, 16, 20, 23, 35, 37, 43, 47, 55, 56, 65, 71, 73, 77, 79, 86, 87, 89, 112, 116]
    cd_data_rep1 = cd_data[cd_data['rep'] == 1]
    cd_data_rep2 = cd_data[cd_data['rep'] == 2]
    cd_data_rep1, cd_data_rep2 = _get_parse_data(cd_id_rep1, cd_id_rep2, cd_data_rep1, cd_data_rep2)

    dd_id_rep1 = [8, 13, 19, 28, 47, 53, 56, 65, 66, 73, 76, 77, 78, 81, 82, 99, 107, 110]
    dd_id_rep2 = [10, 14, 22, 28, 41, 50, 51, 62, 64, 66, 85, 90, 93, 96, 98, 105, 108, 110, 113, 114, 119]
    dd_data_rep1 = dd_data[dd_data['rep'] == 1]
    dd_data_rep2 = dd_data[dd_data['rep'] == 2]
    dd_data_rep1, dd_data_rep2 = _get_parse_data(dd_id_rep1, dd_id_rep2, dd_data_rep1, dd_data_rep2)

    cc_sim = []
    dc_sim = []
    cd_sim = []
    dd_sim = []

    for i in range(20):
        cc_sim.append(pd.read_csv(os.path.join(SIM, 'cc', f'{i}.csv'))['pig.dfi'])
        dc_sim.append(pd.read_csv(os.path.join(SIM, 'dc', f'{i}.csv'))['pig.dfi'])
        cd_sim.append(pd.read_csv(os.path.join(SIM, 'cd', f'{i}.csv'))['pig.dfi'])
        dd_sim.append(pd.read_csv(os.path.join(SIM, 'dd', f'{i}.csv'))['pig.dfi'])

    print('-----')
    _aggregate_corr(cc_data_rep1, cc_data_rep2, cc_sim, 'cc', type='DFI')
    print('-----')
    _aggregate_corr(dc_data_rep1, dc_data_rep2, dc_sim, 'dc', type='DFI')
    print('-----')
    _aggregate_corr(cd_data_rep1, cd_data_rep2, cd_sim, 'cd', type='DFI')
    print('-----')
    _aggregate_corr(dd_data_rep1, dd_data_rep2, dc_sim, 'dd', type='DFI')
    print('-----')

    print('\n')
    print('-----')
    _aggregate_corr(
        [_diff_cfi(d.cumsum()) for d in cc_data_rep1],
        [_diff_cfi(d.cumsum()) for d in cc_data_rep2],
        [_diff_cfi(d.cumsum()) for d in cc_sim],
        prefix='cc',
        type='CFI'
    )
    print('-----')
    _aggregate_corr(
        [_diff_cfi(d.cumsum()) for d in dc_data_rep1],
        [_diff_cfi(d.cumsum()) for d in dc_data_rep2],
        [_diff_cfi(d.cumsum()) for d in dc_sim],
        prefix='dc',
        type='CFI'
    )
    print('-----')
    _aggregate_corr(
        [_diff_cfi(d.cumsum()) for d in cd_data_rep1],
        [_diff_cfi(d.cumsum()) for d in cd_data_rep2],
        [_diff_cfi(d.cumsum()) for d in cd_sim],
        prefix='cd',
        type='CFI'
    )
    print('-----')
    _aggregate_corr(
        [_diff_cfi(d.cumsum()) for d in dd_data_rep1],
        [_diff_cfi(d.cumsum()) for d in dd_data_rep2],
        [_diff_cfi(d.cumsum()) for d in dd_sim],
        prefix='dd',
        type='CFI'
    )
    print('-----')
    

if __name__ == '__main__':
    _setup()
    _parse_data()
    _parse_sim()
    _calc_corr()