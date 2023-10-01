import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

experiments = {
    'cc': [],
    'dc': [],
    'cd': [],
    'dd': []
}

for i in range(20):
    with open(f'result-{i}.txt') as file:
        lines = file.readlines()
        for line in lines:
            line_data = line.split(': ')
            if len(line_data) == 2 and line_data[0] == 'Avg DFI CC Correlation Total':
                experiments['cc'].append((sum(experiments['cc']) + float(line_data[1])) / (i + 1))
            if len(line_data) == 2 and line_data[0] == 'Avg DFI DC Correlation Total':
                experiments['dc'].append((sum(experiments['dc']) + float(line_data[1])) / (i + 1))
            if len(line_data) == 2 and line_data[0] == 'Avg DFI CD Correlation Total':
                experiments['cd'].append((sum(experiments['cd']) + float(line_data[1])) / (i + 1))
            if len(line_data) == 2 and line_data[0] == 'Avg DFI DD Correlation Total':
                experiments['dd'].append((sum(experiments['dd']) + float(line_data[1])) / (i + 1))

plt.plot(range(20), experiments['cc'])
plt.savefig('dfi-cc.png')
plt.clf()
plt.plot(range(20), experiments['dc'])
plt.savefig('dfi-dc.png')
plt.clf()
plt.plot(range(20), experiments['cd'])
plt.savefig('dfi-cd.png')
plt.clf()
plt.plot(range(20), experiments['dd'])
plt.savefig('dfi-dd.png')
plt.clf()

experiments = {
    'cc': [],
    'dc': [],
    'cd': [],
    'dd': []
}

for i in range(20):
    with open(f'result-{i}.txt') as file:
        lines = file.readlines()
        for line in lines:
            line_data = line.split(': ')
            if len(line_data) == 2 and line_data[0] == 'Avg CFI CC Correlation Total':
                experiments['cc'].append((sum(experiments['cc']) + float(line_data[1])) / (i + 1))
            if len(line_data) == 2 and line_data[0] == 'Avg CFI DC Correlation Total':
                experiments['dc'].append((sum(experiments['dc']) + float(line_data[1])) / (i + 1))
            if len(line_data) == 2 and line_data[0] == 'Avg CFI CD Correlation Total':
                experiments['cd'].append((sum(experiments['cd']) + float(line_data[1])) / (i + 1))
            if len(line_data) == 2 and line_data[0] == 'Avg CFI DD Correlation Total':
                experiments['dd'].append((sum(experiments['dd']) + float(line_data[1])) / (i + 1))

plt.plot(range(20), experiments['cc'])
plt.savefig('cfi-cc.png')
plt.clf()
plt.plot(range(20), experiments['dc'])
plt.savefig('cfi-dc.png')
plt.clf()
plt.plot(range(20), experiments['cd'])
plt.savefig('cfi-cd.png')
plt.clf()
plt.plot(range(20), experiments['dd'])
plt.savefig('cfi-dd.png')
plt.clf()
