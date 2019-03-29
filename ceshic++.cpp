#include "Python.h"
#include <iostream> 
int main(int argc, char** argv) 
{char* picpath ="/home/pdd/PD/c++/c++python/pic/0.0.jpg"; 
Py_Initialize(); 
if ( !Py_IsInitialized() ) 
{ return -1; } 
PyRun_SimpleString("import sys"); 
PyRun_SimpleString("sys.path.append('./')"); 
PyObject* pMod = NULL;
 PyObject* pFunc = NULL;
 PyObject* pParm = NULL; 
PyObject* pRetVal = NULL;
char iRetVal=100; 
char* modulName="c++diaoyong"; 
//这个是被调用的py文件模块名字 
pMod = PyImport_ImportModule(modulName); 
if(!pMod) { return -1; } 
char* funcName="evaluate"; 
//这是此py文件模块中被调用的函数名字 
pFunc = PyObject_GetAttrString(pMod, funcName);
 if(!pFunc) { return -2; }
 pParm = PyTuple_New(1); 
PyTuple_SetItem(pParm, 0, Py_BuildValue("s",picpath));
//传入的参数，是图片的路径 
pRetVal = PyEval_CallObject(pFunc, pParm);
//这里开始执行py脚本 
PyArg_Parse(pRetVal, "i", &iRetVal);
//py脚本返回值给iRetVal //PyErr_Print();
 std::cout<<iRetVal;
std::cout<<"yes";
 return iRetVal; }
