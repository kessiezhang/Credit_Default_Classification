def draw_plot(data, column,title,rotation):
    '''
    A function to generate category count plot
    with "Default" as hue
    Input: column name, plot title, x ticks rotation degree
    '''
    plt.figure(figsize=(25,8))
    sns.set_style("darkgrid")
    sns.countplot(data=data,x=column, hue = 'Default', order=data[column].value_counts().index,palette=('Blues_d'))
    sns.set_context("poster")
    plt.ylabel('Number of Users')
    plt.xlabel('')
    plt.title(title)
    plt.xticks(rotation=rotation)
    sns.despine()
    plt.legend(loc=1, ncol=2)
    
def draw_boxplot(x, y, title):
    '''
    A funtion to generate boxplot comparison 
    with "Default" as hue
    Input: x='Default',y and title
    '''
    plt.figure(figsize=(25,7))
    sns.boxplot(
                x= x,
                y= y,
                data=dataset
                )
    plt.title(title)
    plt.ticklabel_format(style='plain', axis='y',useOffset=False);