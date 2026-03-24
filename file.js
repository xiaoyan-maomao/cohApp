function set(path, content){
    localStorage.setItem(path,content)
}

function get(path){
    return localStorage.getItem(path)
}