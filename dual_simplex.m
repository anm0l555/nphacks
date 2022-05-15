clear all;
clc;
format short;
%min z 3x1+5x2
%st
%x1+3x2>=3
%x1+x2>=2
A=[-1 -3 1 0 -3;-1 -1 0 1 -2]
B=[-3;-2]
c=[-3 -5 0 0 0]
bv=[3 4]
variables={'x1', 'x2', 's1', 's2', 'b'} 
zjcj=c(bv)*A-c;
 
A
zjcj
run=true;
[zjcj;A]
while run
    if any(A(:,size(A,2))<0)
        fprintf('not feasible');
 
        for i=1:size(A,2)-1
            [leav,pvt_row]=min(A(:,size(A,2)));
            if A(pvt_row,i)<0
                m(i)=zjcj(i)/A(pvt_row,i);
            else
                m(i)=-inf;
 
            end
        end
 
        [ent,pvt_col]=max(m);
        pvt_val=A(pvt_row,pvt_col);
        bv(pvt_row)=pvt_col
        A(pvt_row,:)=A(pvt_row,:)/pvt_val;
        for i=1:size(A,1)
            if i~=pvt_row
                zjcj=zjcj-zjcj(pvt_col)*A(pvt_row,:);
                A(i,:)=A(i,:)-A(pvt_row,:)*A(i,pvt_col);
            end
        end
        [zjcj;A]
 
    else
        run=false;
    end
end
bv
fprintf('Final simplex table of negative of given objective function:\n');
[zjcj;A]
fprintf('Optimal value will be: %f\n',zjcj(end)*-1)
fprintf('the basic variable values are: \n');
for i=1:size(bv, 2)
fprintf('%s', variables{bv(i)})
fprintf('= %f \n', A(i, end));
end