 T = readtable('Book2.xlsx');
 
 t0=table2array(T(:,1));
 
 temp1=table2array(T(:,2));
 t1=grp2idx(temp1);
 
 temp2=table2array(T(:,3));
 t2=grp2idx(temp2);
 
 temp3=table2array(T(:,4));
 t3=grp2idx(temp3);
 
 t4=table2array(T(:,5:24));
 
 temp4=table2array(T(:,25:31));
 for i=1:125596
     for j=1:7
        t5(i,j)=str2double(temp4{i,j});
     end
 end
 
 t6=table2array(T(:,32:33));
 
 temp5=table2array(T(:,34:41));
 for i=1:125596
     for j=1:8
        t7(i,j)=str2double(temp5{i,j});
     end
 end
 
 temp6=table2array(T(:,42));
 t8=grp2idx(temp6);
 
 data1=[t0 t1 t2 t3 t4 t5 t6 t7 t8];

 save('data1.mat','data1');
 
 data2=[normalize(data1(:,1:41),'range') data1(:,42)];
 
 save('data2.mat','data2');
 
 count=1;
 count2=1;
 for i=1:10
     locs=find(data2(:,42)==i);
     percent=floor(length(locs)*0.1);
     rands=randperm(length(locs),percent);
     
     for j=1:length(rands)
         test(count,:)=data2(locs(rands(j)),:);
         count=count+1;
     end
     
     locs2=locs;
     locs2(rands)=[];
     
     for k=1:length(locs2)
         train(count2,:)=data2(locs2(k),:);
         count2=count2+1;
     end
   
 end
 
 save('train.mat','train');
 
 save('test.mat','test');
 