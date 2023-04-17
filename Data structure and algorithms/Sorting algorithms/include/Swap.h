template <class T>
void swap(T &v1, T &v2){
    auto tmp = v1;
    v1 = v2;
    v2 = tmp;
}