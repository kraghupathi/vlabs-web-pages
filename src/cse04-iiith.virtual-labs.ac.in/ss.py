f=open("template.html",'r')
template=f.read()
s=""
with open('index.php?section=List%20of%20experiments', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
    
   
    
f=open('experiments.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)
f.seek(0)
content=f.read()
print content
filedata=content.replace('index.php','introduction.html')
f.seek(0)
f.write(filedata)

content.replace('index.php','intrdocuct')
s=""
with open('index.php?section=Introduction', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('introduction.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Feedback', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('feedback.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Prerequisite%20S%2FW', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('prerequisites.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Courses%20Aligned', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('courses_aligned.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)

s=""
with open('index.php?section=Target%20Audience', 'r') as f:
    content = f.read()
    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
    t= content.index('</section>')
    f.seek(content.index('<div id="experiment-article-section-1-heading" class="heading">'))
    s= f.read(t-k)
    print s
    
f=open('target_audience.html', 'w+')
f.write(template)
f.seek(0)
content = f.read()
k=content.index('<div class="col-md-10 lab-list-col-10">')
t= content.index('<!--edit -->')
f.seek(t+13)
s=s+f.read()
f.seek(t+13)
f.write(s)
