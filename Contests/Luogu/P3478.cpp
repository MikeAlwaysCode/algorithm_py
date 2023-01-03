const int maxn=1000005;

int n;
std::vector<int>v[maxn];

int dep[maxn],siz[maxn],f[maxn];//这里的f就是上面的sum数组
void dfs1(const int x,const int fa){
  dep[x]=dep[fa]+1;
  siz[x]=1;
  for(int i=0;i<v[x].size();++i){
    int y=v[x][i];
    if(y==fa) continue;
    dfs1(y,x);
    siz[x]+=siz[y];//统计出siz数组
  }
}
void dfs2(const int x,const int fa){
  for(int i=0;i<v[x].size();++i){
    int y=v[x][i];
    if(y==fa) continue;
    f[y]=f[x]+n-2*siz[y];//从父亲向儿子转移
    dfs2(y,x);
  }
}

signed main(){
  // freopen("simpleinput.txt","r",stdin);
  read(n);
  for(int i=1,x,y;i<n;++i){
    read(x),read(y);
    v[x].push_back(y),v[y].push_back(x);
  }
  dfs1(1,0);
  for(int i=1;i<=n;++i)
    f[1]+=dep[i];//统计出根的sum来
  dfs2(1,0);
  int ans,mx=0;
  for(int i=1;i<=n;++i)
    if(f[i]>mx) ans=i,mx=f[i];
  write(ans),putchar('\n');
  return 0;
}
