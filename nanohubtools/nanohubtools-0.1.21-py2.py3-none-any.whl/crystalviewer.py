from .rappturetool import Rappturetool, __file__
from ipywidgets import HBox, VBox, HTML, Image, Layout, Button, ButtonStyle, Tab, Output, Box
from IPython.display import HTML, Javascript, clear_output
from hublib import ui
from .plotlywidget import FigureWidget       
import uuid, weakref, inspect, time
import xml.etree.ElementTree as ET
import hashlib, json
import math, os, base64
import numpy as np
import pythreejs as pt

class CrystalViewerTool (Rappturetool):
    parameters_miller = [            
        'Draw_miller_plane',
        'Draw_plane_1',
        'Miller_index_1_1',
        'Miller_index_1_2',
        'Miller_index_1_3',
        'Draw_plane_2',
        'Miller_index_2_1',
        'Miller_index_2_2',
        'Miller_index_2_3',
        'Draw_plane_3',
        'Miller_index_3_1',
        'Miller_index_3_2',
        'Miller_index_3_3',
    ]
    
    parameters_additional = [
        'What_to_do'
    ]        

    def __init__(self, credentials, parameters, **kwargs):
        kwargs.setdefault('title', 'CrystalViewer')
        Rappturetool.__init__(self, credentials, "crystal_viewer", parameters, extract_method="id", **kwargs)
            
    def displayMillerOptions(self):
        milleropt = VBox(layout=Layout(width='100%', height='100%'))    
        self.millertab = Tab()
        millerchildren = []
        for i in range(0,3):
            container_miller = VBox(layout=Layout(width='100%', height='100%'))    
            mparameters = ['Draw_plane_'+ str(i+1),
            'Miller_index_'+ str(i+1)+'_1',
            'Miller_index_'+ str(i+1)+'_2',
            'Miller_index_'+ str(i+1)+'_3']
            children_miller = []
            for p in mparameters:
                if p in self.parameters_miller :
                    if p in self.options:
                        children_miller.append(self.options[p])
            container_miller.children = children_miller
            millerchildren.append(container_miller)
            self.options['Draw_plane_'+ str(i+1)].dd.observe(lambda b, this=self : this.showMillerPlane(this.options['Draw_miller_plane'].value), 'value')
            
        self.millertab.children = millerchildren
        for i in range(0,3):
            self.millertab.set_title(i, "Plane" + str(i+1))    
        self.options['Draw_miller_plane'].dd.observe(lambda b, this=self : this.showMillerPlane(b['new']), 'value')
        milleropt.children = [self.options['Draw_miller_plane'], self.millertab, self.options_but]
        return milleropt

    def showMillerPlane (self, value):
        enabled = (value == "yes")
        if enabled is True:
            value_display = None
        else:
            value_display = 'none'
        for opt in self.parameters_miller:
            if opt != 'Draw_miller_plane':
                self.options[opt].visible = enabled
                self.options[opt].layout.display = value_display
        for opt in self.parameters_miller:
            if opt != 'Draw_miller_plane':
                self.options[opt].visible = enabled
                self.options[opt].layout.display = value_display            
        self.millertab.visible = enabled
        self.millertab.layout.display = value_display
        if enabled:
            for i in range(0,3):
                mparameters = [
                    'Miller_index_'+ str(i+1)+'_1',
                    'Miller_index_'+ str(i+1)+'_2',
                    'Miller_index_'+ str(i+1)+'_3'
                ]
                enabled = (self.options['Draw_plane_'+ str(i+1)].value == "yes")
                if enabled is True:
                    value_display = None
                else:
                    value_display = 'none'
                for opt in mparameters:
                    if opt in self.options:
                        self.options[opt].visible = enabled
                        self.options[opt].layout.display = value_display

                        

        
class CrystalViewerMaterial (CrystalViewerTool):
    def __init__(self, credentials, **kwargs):
                                            
        self.parameters_structure = [
            '_Structure', 
            'Crystal_structure',
            #'Crystal_system',
            '1','2','3','4','5','6','7','8','9','10','11','12',
            'Nx',
            'Ny',
            'Nz',
            'Primitive_cell',

            'Lx',
            'Ly',
            'Number_of_sheet',
            'C_C_bong_length',
            'Separation_distance',
            'AA_Stacking',
            
            'n',
            'm',
            'num_of_unit_cell',
            'Number_of_sheet',
        ]
        CrystalViewerTool.parameters_miller = CrystalViewerTool.parameters_miller
        self.parameters_additional = self.parameters_additional
        parameters = self.parameters_structure + self.parameters_miller + self.parameters_additional
        kwargs.setdefault('title', 'CrystalViewer - Materials')
        CrystalViewerTool.__init__(self, credentials, parameters, **kwargs)
        self.reset_options = False

    def showMaterial (self, id):
        for i in range(1,13):
            if (i == id):
                self.options[str(i)].visible = True
                self.options[str(i)].layout.display = None
            else:
                self.options[str(i)].visible = False
                self.options[str(i)].layout.display = 'none'
        for opt in ['Nx','Ny','Nz']:
            if id == 8:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'
            else:
                self.options[opt].visible = True
                self.options[opt].layout.display = None
                
        for opt in ['Lx','Ly','Number_of_sheet','Separation_distance','AA_Stacking']:
            if id == 8 and self.options['8'].value == '1':
                self.options[opt].visible = True
                self.options[opt].layout.display = None
            else:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'
            
        for opt in ['n','m','num_of_unit_cell','Number_of_sheet']:
            if id == 8 and self.options['8'].value == '2':
                self.options[opt].visible = True
                self.options[opt].layout.display = None
            else:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'
                
        for opt in ['C_C_bong_length']:
            if id == 8 and ( self.options['8'].value == '2' or self.options['8'].value == '1'):
                self.options[opt].visible = True
                self.options[opt].layout.display = None
            else:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'        
                
    def displayOptions(self):
        html = '''
        <b>Visualize crystalline structure of different materials and Bravais lattice</b>
        '''
        container_structure = VBox(layout=Layout(width='100%', height='100%'))
        children_structure = []
        
        children_structure.append(HTML(value=html))

        for p in self.parameters_structure :
            if p in self.options:            
                children_structure.append(self.options[p])
            else:
                children_structure.append(Button(description=p.replace('_',''),layout=Layout(width='auto'),style=ButtonStyle(button_color='lightblue')))

                               
        self.options['Crystal_structure'].dd.observe(lambda b, this=self : this.showMaterial(int(b['new'])), 'value')

        children_structure.append(self.options_but)
        container_structure.children = children_structure
        #container_introduction.children = children_introduction
        container_miller = self.displayMillerOptions()
        self.showMaterial(1)
        self.showMillerPlane(False)
        crystaltab = Tab()
        
        crystaltab.children = [container_structure, container_miller]
        crystaltab.set_title(0, "Structure")
        crystaltab.set_title(1, "Miller Planes")
                
        self.options_cont.children = [crystaltab]                
        
class CrystalViewerBravais (CrystalViewerTool):
    def __init__(self, credentials, **kwargs):
                                            
        self.parameters_structure = [
            '_Structure', 
            'Crystal_system',
            '_Bravais Lattice',
            '21','22','23','24','25','26','27',
            '_Bravais Lattice Parameters',            
            'a',
            'b',
            'c',
            'Alpha',
            'Beta',
            'Gamma',
            '_Dimension',
            'Nx',
            'Ny',
            'Nz',
        ]
        CrystalViewerTool.parameters_miller = CrystalViewerTool.parameters_miller
        self.parameters_additional = self.parameters_additional
        parameters = self.parameters_structure + self.parameters_additional
        kwargs.setdefault('title', 'CrystalViewer - Bravais')
        CrystalViewerTool.__init__(self, credentials, parameters, **kwargs)
        self.reset_options = False

    def showBravais (self, id):
        options = {
            'a' : [21,22,23,24,25,26,27],
            'b' : [21,22,23],
            'c' : [21,22,23,24,26],
            'Alpha' : [21,27],
            'Beta' : [21,22],
            'Gamma' : [21]
        }

        for d in range (21,28):
            if (id == d):
                self.options[str(d)].visible = True
                self.options[str(d)].layout.display = None
            else:
                self.options[str(d)].visible = False
                self.options[str(d)].layout.display = 'none'

        for key, value in options.items():
            if (id in value):
                self.options[key].visible = True
                self.options[key].layout.display = None
            else:
                self.options[key].visible = False
                self.options[key].layout.display = 'none'
     
                
    def displayOptions(self):
        html = '''
        <b>Visualize crystalline structure of different materials and Bravais lattice</b>
        '''
        container_structure = VBox(layout=Layout(width='100%', height='100%'))
        children_structure = []
        
        children_structure.append(HTML(value=html))

        for p in self.parameters_structure :
            if p in self.options:            
                children_structure.append(self.options[p])
            else:
                children_structure.append(Button(description=p.replace('_',''),layout=Layout(width='auto'),style=ButtonStyle(button_color='lightblue')))

                               
        self.options['Crystal_system'].dd.observe(lambda b, this=self : this.showBravais(int(b['new'])), 'value')

        children_structure.append(self.options_but)
        container_structure.children = children_structure
        self.showBravais(int(self.options['Crystal_system'].value))
        crystaltab = Tab()
        
        crystaltab.children = [container_structure]
        crystaltab.set_title(0, "Structure")
        crystaltab.set_title(1, "Miller Planes")
                
        self.options_cont.children = [crystaltab]
        self.options[self.parameters_additional[0]].value = '3'
        
class CrystalViewerConstructor (CrystalViewerTool):
    def __init__(self, credentials, **kwargs):
                                            
        self.parameters_structure = [
            '_Structure', 
            'Basis_atom_number',
            
            '_Basis Atoms',             
            'Atom_1_position',
            'Atom_1_type',
            'Atom_2_position',
            'Atom_2_type',
            'Atom_3_position',
            'Atom_3_type',
            'Atom_4_position',
            'Atom_4_type',
            'Atom_5_position',
            'Atom_5_type',
            'Atom_6_position',
            'Atom_6_type',
            'Atom_7_position',
            'Atom_7_type',
            'Atom_8_position',
            'Atom_8_type',
            
            '_Bravais vector',             
            'Vector_1',
            'Vector_2',
            'Vector_3',
            
            '_Define Bond Radius',
            'Bond_radius',

            '_Dimensions',
            'Nx_userdefined',
            'Ny_userdefined',
            'Nz_userdefined',
        ]
        CrystalViewerTool.parameters_miller = CrystalViewerTool.parameters_miller
        self.parameters_additional = self.parameters_additional
        parameters = self.parameters_structure + self.parameters_miller + self.parameters_additional
        kwargs.setdefault('title', 'CrystalViewer - Materials')
        CrystalViewerTool.__init__(self, credentials, parameters, **kwargs)
        self.reset_options = False

    def showAtoms (self, id):
        for i in range(1,9):
            for opt in ['Atom_'+str(i)+'_position', 'Atom_'+str(i)+'_type']:
                if (i <= id):
                    self.options[opt].visible = True
                    self.options[opt].layout.display = None
                else:
                    self.options[opt].visible = False
                    self.options[opt].layout.display = 'none'
     
                
    def displayOptions(self):
        html = '''
        <b>Visualize crystalline structure of different materials and Bravais lattice</b>
        '''
        container_structure = VBox(layout=Layout(width='100%', height='100%'))
        children_structure = []
        
        children_structure.append(HTML(value=html))

        for p in self.parameters_structure :
            if p in self.options:            
                children_structure.append(self.options[p])
            else:
                children_structure.append(Button(description=p.replace('_',''),layout=Layout(width='auto'),style=ButtonStyle(button_color='lightblue')))

                               
        self.options['Basis_atom_number'].dd.observe(lambda b, this=self : this.showAtoms(int(b['new'])), 'value')

        children_structure.append(self.options_but)
        container_structure.children = children_structure
        container_miller = self.displayMillerOptions()
        self.showAtoms(int(self.options['Basis_atom_number'].value))
        self.showMillerPlane(False)
        crystaltab = Tab()
        
        crystaltab.children = [container_structure, container_miller]
        crystaltab.set_title(0, "Structure")
        crystaltab.set_title(1, "Miller Planes")
                
        self.options_cont.children = [crystaltab]            
        self.options[self.parameters_additional[0]].value = '2'




class InstanceTracker(object):
    __instances__ = weakref.WeakValueDictionary()

    def __init__(self, *args, **kwargs):
        self.__instances__[id(self)]=self

    @classmethod
    def find_instance(cls, obj_id):
        return cls.__instances__.get(obj_id, None)

        
class CrystalViewerSimplified (InstanceTracker, CrystalViewerTool):
    jcpk = {
        'H'  : 'rgb(255,255,255)',
        'He'  : 'rgb(20,20,20)',
        'Li' : 'rgb(188,190,187)',
        'Be' : 'rgb(134,134,134)',
        'B' : 'rgb(122,117,114)',
        'C' : 'rgb(0,0,0)',
        'N' : 'rgb(32,96,255)',
        'O' : 'rgb(238,32,16)',
        'F' : 'rgb(177,146,82)',
        'Ne' : 'rgb(255,0,0)',
        'Na' : 'rgb(218,220,217)',
        'Mg' : 'rgb(195,195,185)',
        'Al' : 'rgb(192,168,167)',
        'Si' : 'rgb(129,154,154)',
        'P' : 'rgb(255,129,0)',
        'S' : 'rgb(248,239,146)',
        'Cl' : 'rgb(213,221,182)',
        'Ar' : 'rgb(221,112,244)',
        'K' : 'rgb(165,171,171)',
        'Ca' : 'rgb(103,105,110)',
        'Sc' : 'rgb(176,173,166)',
        'Ti' : 'rgb(169,163,147)',
        'V' : 'rgb(191,189,202)',
        'Cr' : 'rgb(191,198,206)',
        'Mn' : 'rgb(206,205,200)',
        'Fe' : 'rgb(185,183,184)',
        'Co' : 'rgb(171,163,160)',
        'Ni' : 'rgb(181,165,150)',
        'Cu' : 'rgb(196,78,46)',
        'Zn' : 'rgb(255,0,0)',
        'Ga' : 'rgb(195,144,144)',
        'Ge' : 'rgb(102,144,144)',
        'As' : 'rgb(190,129,228)',
        'Se' : 'rgb(191,71,75)',
        'Br' : 'rgb(154,32,24)',
        'Kr' : 'rgb(164,162,175)',
        'Rb' : 'rgb(122,119,110)',
        'Sr' : 'rgb(217,206,160)',
        'Y' : 'rgb(153,155,154)',
        'Zr' : 'rgb(153,143,133)',
        'Nb' : 'rgb(98,91,138)',
        'Mo' : 'rgb(93,88,85)',
        'Tc' : 'rgb(131,120,116)',
        'Ru' : 'rgb(153,147,149)',
        'Rh' : 'rgb(156,143,135)',
        'Pd' : 'rgb(162,161,157)',
        'Ag' : 'rgb(177,173,170)',
        'Cd' : 'rgb(106,106,104)',
        'In' : 'rgb(127,109,87)',
        'Sn' : 'rgb(126,120,94)',
        'Sb' : 'rgb(159,99,182)',
        'Te' : 'rgb(150,155,158)',
        'I' : 'rgb(95,98,105)',
        'Xe' : 'rgb(0,0,255)',
        'Cs' : 'rgb(167,170,175)',
        'Ba' : 'rgb(62,71,86)',
        'La' : 'rgb(196,184,172)',
        'Ce' : 'rgb(110,101,94)',
        'Pr' : 'rgb(96,91,97)',
        'Nd' : 'rgb(156,154,155)',
        'Pm' : 'rgb(102,102,102)',
        'Sm' : 'rgb(136,117,100)',
        'Eu' : 'rgb(217,213,204)',
        'Gd' : 'rgb(119,129,105)',
        'Tb' : 'rgb(236,241,235)',
        'Dy' : 'rgb(134,121,102)',
        'Ho' : 'rgb(131,123,121)',
        'Er' : 'rgb(177,182,175)',
        'Tm' : 'rgb(168,163,160)',
        'Yb' : 'rgb(0,255,0)',
        'Lu' : 'rgb(160,161,153)',
        'Hf' : 'rgb(171,188,178)',
        'Ta' : 'rgb(154,155,160)',
        'W' : 'rgb(138,131,123)',
        'Re' : 'rgb(123,123,121)',
        'Os' : 'rgb(185,196,200)',
        'Ir' : 'rgb(137,130,112)',
        'Pt' : 'rgb(210,211,205)',
        'Au' : 'rgb(203,152,53)',
        'Hg' : 'rgb(80,46,48)',
        'Tl' : 'rgb(143,141,142)',
        'Pb' : 'rgb(81,81,81)',
        'Bi' : 'rgb(114,106,103)',
        'Po' : 'rgb(139,153,164)',
        'At' : 'rgb(102,102,102)',
        'Rn' : 'rgb(71,132,0)',
        'Fr' : 'rgb(102,102,102)',
        'Ra' : 'rgb(156,152,125)',
        'Ac' : 'rgb(66,73,224)',
        'Th' : 'rgb(80,73,65)',
        'Pa' : 'rgb(154,147,92)',
        'U' : 'rgb(120,122,119)',
        'Np' : 'rgb(90,73,53)',
        'Pu' : 'rgb(200,200,200)',
        'Am' : 'rgb(117,80,28)',
        'Cm' : 'rgb(62,65,58)',
        'Bk' : 'rgb(208,208,208)',
        'Cf' : 'rgb(231,231,231)',
        'Es' : 'rgb(59,163,200)',
        'Fm' : 'rgb(102,102,102)',
        'Md' : 'rgb(102,102,102)',
        'No' : 'rgb(102,102,102)',
        'Lr' : 'rgb(102,102,102)',
        'Rf' : 'rgb(102,102,102)',
        'Db' : 'rgb(102,102,102)',
        'Sg' : 'rgb(102,102,102)',
        'Bh' : 'rgb(102,102,102)',
        'Hs' : 'rgb(102,102,102)',
        'Mt' : 'rgb(102,102,102)',
    }
    
    def __init__(self, credentials, **kwargs):
        self.engine = kwargs.get("engine", "plotly")
        InstanceTracker.__init__(self)                                  
        self.parameters_structure = [
            'Nx',
            'Ny',
            'Nz',

            'Lx',
            'Ly',
            'Number_of_sheet',
            'C_C_bong_length',
            'Separation_distance',
            'AA_Stacking',
            
            'n',
            'm',
            'num_of_unit_cell',
            'Number_of_sheet',
        ]
        
        self.hashtable = {
        }
        
        self.samples = 16
        self.resize = .15
        self.phi = np.linspace(0, 2*np.pi, self.samples)
        self.theta = np.linspace(-np.pi/2, np.pi/2, self.samples)
        self.thetat = np.linspace(0,2*np.pi,self.samples)
        self.phit = np.linspace(0,np.pi,self.samples)
        self.xt = np.outer(np.cos(self.thetat),np.sin(self.phit)) * 4 * self.resize
        self.yt = np.outer(np.sin(self.thetat),np.sin(self.phit)) * 4 * self.resize
        self.zt = np.outer(np.ones(self.samples),np.cos(self.phit)) * 4 * self.resize
        self.cosphi = np.cos(self.phi) * self.resize
        self.sinphi = np.sin(self.phi) * self.resize
        self.phi, self.theta=np.meshgrid(self.phi, self.theta)
        self.x = np.cos(self.theta) * np.sin(self.phi)
        self.y = np.cos(self.theta) * np.cos(self.phi)
        self.z = np.sin(self.theta)
        self.x = self.x.flatten() * 4 * self.resize
        self.y = self.y.flatten() * 4 * self.resize
        self.z = self.z.flatten() * 4 * self.resize
        
        self.fig = FigureWidget({
            'data': [],
            'layout': { 'height' : 600, 'scene':{'aspectmode':'data'}, 'margin' : {'l':0,'r':0,'t':0,'b':0} }
        })  
        
        self.current_view = "textbook";
        self.hashitem = None;
        self.crystal_component_output = Output(layout=Layout(width="100%", padding="0px"))
        self.parameters_component_output = Output(layout=Layout(height="100%", padding="0px"))
        self.content_component_output = Output(layout=Layout(flex='1', padding="0px", overflow="scroll"))
        self.ref = id(self)
        self.parameters_additional = [
            'Primitive_cell',
            'Crystal_structure',
            '1','2','3','4','5','6','7','8','9','10','11','12',            
        ]

        self.parameters_miller = CrystalViewerTool.parameters_miller
        self.parameters_additional = self.parameters_additional
        parameters = self.parameters_structure + self.parameters_miller + self.parameters_additional
        kwargs.setdefault('title', 'CrystalViewer - Materials')
        CrystalViewerTool.__init__(self, credentials, parameters, **kwargs)
        self.reset_options = False
        

    def showMaterial (self, id):
        for i in range(1,13):
            if (i == id):
                self.options[str(i)].visible = True
                self.options[str(i)].layout.display = None
            else:
                self.options[str(i)].visible = False
                self.options[str(i)].layout.display = 'none'
                self.options[str(i)].value = self.parameters[str(i)]['default']

        for opt in ['Nx','Ny','Nz']:
            if id == 8:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'
            else:
                self.options[opt].visible = True
                self.options[opt].layout.display = None
                self.options[opt].value = self.parameters[opt]['default']
                
        for opt in ['Lx','Ly','Number_of_sheet','Separation_distance','AA_Stacking']:
            if id == 8 and self.options['8'].value == '1':
                self.options[opt].visible = True
                self.options[opt].layout.display = None
            else:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'
                self.options[opt].value = self.parameters[opt]['default']
            
        for opt in ['n','m','num_of_unit_cell','Number_of_sheet']:
            if id == 8 and self.options['8'].value == '2':
                self.options[opt].visible = True
                self.options[opt].layout.display = None
            else:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'
                self.options[opt].value = self.parameters[opt]['default']
                
        for opt in ['C_C_bong_length']:
            if id == 8 and ( self.options['8'].value == '2' or self.options['8'].value == '1'):
                self.options[opt].visible = True
                self.options[opt].layout.display = None
            else:
                self.options[opt].visible = False
                self.options[opt].layout.display = 'none'        
                self.options[opt].value = self.parameters[opt]['default']


    def buildCrystal(self):   
        crystal_component_view = '''
        <style>
        
        .CrystalViewerLogo{
            line-height : normal;
            width : 140px ;
            height : 140px; 
            font-size : 20px ; 
            display : flex;
            flex-direction : column;
            justify-content : center;
            text-align : center;
            border-right : 4px solid #FFFFFF;
            color : #707070;
            background-image: url("data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9JzMwMHB4JyB3aWR0aD0nMzAwcHgnICBmaWxsPSIjMDAwMDAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTAwIDEwMCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+PGc+PGc+PHBvbHlnb24gcG9pbnRzPSIzNC40LDM5LjcgNDQuNyw4Ni45IDUwLjUsOTUgNTQuMSw0Mi41ICAgIj48L3BvbHlnb24+PC9nPjxnPjxwb2x5Z29uIHBvaW50cz0iNDUsMzEuNCAzNS4xLDM4LjggNTMuNCw0MS40ICAgIj48L3BvbHlnb24+PC9nPjxnPjxwb2x5Z29uIHBvaW50cz0iNjMuMywyNi42IDUxLjUsNSA0NS44LDMwLjEgICAiPjwvcG9seWdvbj48L2c+PGc+PHBvbHlnb24gcG9pbnRzPSI2NS42LDQwLjUgNjMuOCwyOC40IDU1LjYsNDEuNSAgICI+PC9wb2x5Z29uPjwvZz48Zz48cG9seWdvbiBwb2ludHM9IjQ5LjksNy43IDM1LjEsMzcuNSA0NC43LDMwLjQgICAiPjwvcG9seWdvbj48L2c+PGc+PHBvbHlnb24gcG9pbnRzPSI1MS44LDkxLjQgNjUuNSw0MS42IDU1LjEsNDIuNiAgICI+PC9wb2x5Z29uPjwvZz48Zz48cG9seWdvbiBwb2ludHM9IjU0LjYsNDEuMiA2MywyNy43IDQ2LjEsMzEuMSAgICI+PC9wb2x5Z29uPjwvZz48L2c+PC9zdmc+");
            background-size: 120px;
            background-repeat: no-repeat;
            background-position-x: -30px;
            background-position-y: 10px;
            padding-left: 30px;
        }

                        
        .ComponentMaterialSelected, .ComponentMaterial{
            height: 35px;
            border-radius: 15px;
            border: 1px solid #707070;
            color: #707070;
            padding: 10px 20px 10px 20px;
            background-color: #FFF;
            font-size:15px;
        }

        .ComponentMaterialSpace{
            width:6px;
            padding:0px;
        }
        
        .ComponentMaterialSelected, .ComponentMaterial:hover{
            background-color:#B6BEFD;
        }

        .ComponentCrystalSelected, .ComponentCrystal{
            height: 60px;
            width: 60px;
            border-radius:60px;
            background-color:#FFFFFF;
            border:1px solid #707070;
        }

        .ComponentCrystalSpace{
            width:6px;
            padding:0px;
        }
        
        .ComponentCrystalSelected, .ComponentCrystal:hover{
            background-color:#B6BEFD;
        }

        .ComponentCrystals{
            display:flex;
            flex-direction:row;
            justify-content:flex-start;
            padding-top: 10px;       
            padding-bottom: 10px;
        }

        .ComponentMaterials{
            display:flex;
            flex-direction:row;
            justify-content:flex-start;
            padding-top: 10px;
            border-top: 1px solid #707070;            
        }
        
        .materialsTitle{
            display: flex;
            flex-direction: column;
            text-align: left;
            justify-content: flex-start;
            font-size: 15px;
            color: #707070;
            width: 100px;
            padding-left: 10px;
        }
        
        div.output_subarea{
            padding:0px
        }
                    

        .crystal1{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal1.png") + ''';
        }

        .crystal2{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal2.png") + ''';
        }

        .crystal3{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal3.png") + ''';
        }

        .crystal4{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal4.png") + ''';
        }

        .crystal5{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal5.png") + ''';
        }

        .crystal6{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal6.png") + ''';
        }

        .crystal7{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal7.png") + ''';
        }

        .crystal8{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal8.png") + ''';
        }

        .crystal9{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal9.png") + ''';
        }

        .crystal10{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal10.png") + ''';
        }

        .crystal11{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal11.png") + ''';
        }

        .crystal12{
            background-size: 50px 50px;
            background-repeat:no-repeat;
            background-position: center center;
            background-image: ''' + self.buildIcon("crystal12.png") + ''';
        }

        </style>
        <div id="crystal_''' + str(self.ref) + '''"></div>
        '''


        crystal_component_js = '''
        requirejs.config({
            paths: {
                'react': 'https://unpkg.com/react@16.8.6/umd/react.development',
                'react-dom': 'https://unpkg.com/react-dom@16/umd/react-dom.development'
            }
        });

        requirejs(['react', 'react-dom'], function(React, ReactDOM) {
            class Util {
                static create_UUID(){
                    var dt = new Date().getTime();
                    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
                        var r = (dt + Math.random()*16)%16 | 0;
                        dt = Math.floor(dt/16);
                        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
                    });
                    return uuid;
                }
            }

 
            class CrystalsComponent extends React.Component {
                constructor(props) {
                    super(props)
                    this.state = { 
                        crystals:{
                            "Diamond":{
                                "materials":["Si","Ge"],
                                "icon": "crystal1",
                                "default":"Si",
                                "value": "1",
                            },
                            "Zincblende":{
                                "materials":["AlP","AlAs","AlSb","GaAs","GaP", "GaSb", "InAs", "InP", "InSb"],
                                "icon": "crystal2",
                                "default":"GaAs",
                                "value": "2",
                            },
                            "Wurtzite":{
                                "materials":["AlN","InN","GaN"],
                                "icon": "crystal3",
                                "default":"GaN",
                                "value": "3",
                            },
                            "Sodium Chloride":{
                                "materials":["NaCl","SmSe"],
                                "icon": "crystal4",
                                "default":"NaCl",
                                "value": "4",
                            },
                            "Cesium Chloride":{
                                "materials":["CsCl"],
                                "icon": "crystal5",
                                "default":"CsCl",
                                "value": "5",
                            },
                            "Face-centered cubic":{
                                "materials":["Cu", "Al","Ag","Au"],
                                "icon": "crystal6",
                                "default":"Cu",
                                "value": "6",
                            },
                            "Body-centered cubic":{
                                "materials":["W"],
                                "icon": "crystal7",
                                "default":"W",
                                "value": "7",
                            },
                            "Carbon meshes":{
                                "materials":["Graphene", "Carbon nanotube", "Bucky ball(C60)"],
                                "icon": "crystal8",
                                "default":"Graphene",
                                "value": "8",
                            },
                            "Rhombohedral":{
                                "materials":["Bi2Te3"],
                                "icon": "crystal9",
                                "default":"Bi2Te3",
                                "value": "9",
                            },
        //                    "Perovskite":{
        //                        "materials":["SrTiO3"],
        //                        "icon": "crystal10",
        //                        "default":"SrTiO3",
        //                        "value": "10",
        //                    },
                            "TMD":{
                                "materials":["MoS2"],
                                "icon": "crystal11",
                                "default":"MoS2",
                                "value": "11",
                            },                     
                            "Black Phosphorous":{
                                "materials":["Black Phosphorous"],
                                "icon": "crystal12",
                                "default":"Black Phosphorous",
                                "value": "12",
                            },                
                        }, 
                        selectedCrystal:"Diamond",
                        selectedMaterial:"Si",
                        showMaterials: true,
                    } 
                }    

                selectCrystal(crystal){
                    this.setState({
                        selectedCrystal:crystal, 
                        selectedMaterial:this.state.crystals[crystal].default,
                        showMaterials: true
                    })
                    if (crystal == "Carbon meshes")
                        CrystalViewerSimplified_''' + str(self.ref) + '''['exposedSelectMaterial'](this.state.crystals[crystal].value, 1)
                    else
                        CrystalViewerSimplified_''' + str(self.ref) + '''['exposedSelectMaterial'](this.state.crystals[crystal].value, this.state.crystals[crystal].default)
                }

                selectMaterial(material){
                    material = material + ""
                    this.setState({
                        selectedMaterial:material,
                    })
                    var sc = this.state.selectedCrystal
                    CrystalViewerSimplified_''' + str(self.ref) + '''['exposedSelectMaterial'](this.state.crystals[sc].value, material)
                }

                showMaterials( status ){
                    if (status == undefined)
                        status = !this.state.showMaterials
                    this.setState({
                        showMaterials: status
                    })
                }

                render(){
                    var children = Array()    
                    let self = this
                    children.push(React.createElement("div", {key:Util.create_UUID(), className:"materialsTitle"}, "Crystals"))
                    for (let crystal in this.state.crystals) {
                        var crystal_instance = this.state.crystals[crystal]
                        let cur_crystal = crystal
                        if (crystal != this.state.selectedCrystal){
                            children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentCrystal " + crystal_instance.icon, style:style, onClick:function(e){self.selectCrystal(crystal)}, title:crystal}))
                        } else {
                            children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentCrystalSelected " + crystal_instance.icon, style:style, onClick:function(e){self.showMaterials()}, title:crystal}))
                        }                
                        children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentCrystalSpace"}))
                    }  
                    var mat_children = Array()    
                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"materialsTitle"}, "Materials"))
                    
                    if (this.state.showMaterials){
                        var materials = this.state.crystals[this.state.selectedCrystal].materials
                        for (let index in materials) {
                            let material = materials[index]
                            var style = {
                                display: "flex",
                                alignItems: "center",
                                flexDirection: "row",
                                justifyContent: "center",
                            }
                            if (this.state.selectedCrystal == 'Carbon meshes'){
                                if ((index+1) != this.state.selectedMaterial){
                                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentMaterial", style:style, onClick:function(e){self.selectMaterial(parseInt(index)+1)}, title:material}, material))                                
                                } else {
                                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentMaterialSelected", style:style, title:material}, material))
                                }                
                            } else {
                                if (material != this.state.selectedMaterial){
                                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentMaterial", style:style, onClick:function(e){self.selectMaterial(material)}, title:material}, material))                                
                                } else {
                                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentMaterialSelected", style:style, title:material}, material))
                                }                
                            }
                            mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentMaterialSpace"}))
                        }            
                    }
                    var crystals = React.createElement("div", {key:Util.create_UUID(), className:"ComponentCrystals"}, children)
                    var materials = React.createElement("div", {key:Util.create_UUID(), className:"ComponentMaterials"}, mat_children)
                    var mat_container = React.createElement("div", {key:Util.create_UUID(), className:"", style:{flex:1}}, [crystals, materials])

                    var title = React.createElement("div", {key:Util.create_UUID(), className:"CrystalViewerLogo", style:{}}, "Crystal Viewer")

                    var div = React.createElement("div", {key:Util.create_UUID(), className:"", style:{backgroundColor:'#EEEEEE', display:'flex',flexDirection: 'row',}}, [title, mat_container])

                    return div
                }
            }

            ReactDOM.render(
                React.createElement(CrystalsComponent, {}),
                document.getElementById("crystal_''' + str(self.ref) + '''")
            );
        });
        '''        
       
        return crystal_component_view, crystal_component_js

    def buildIcon(self, icon):
        path = os.path.dirname(__file__)
        image_encoded = ""
        with open(path+"/assets/" + icon,'rb' ) as f:
            image_encoded = f.read()                    
        image = base64.encodebytes(image_encoded).decode("utf-8") 
        html = "url(data:image/png;base64," + str(image).replace("\n", "").replace("=", "") +")"
        return json.loads(json.dumps(html))

        
        
    def buildParameters(self):    
        parameter_component_view = '''
        <style>
        .ComponentOptionSelected, .ComponentOption{
            height: 35px;
            width: 130px;
            border-radius:15px;
            background-color: #FFFFFF;
            border:1px solid #707070;  
            font-size: 15px;
            color : #707070;
        }

        .ComponentOptionSelected, .ComponentOption:hover{
            background-color: #B6BEFD;
        }

        .ComponentOptionSpacer{
            height: 10px;
        }
        
        .ComponentSubOptionSelected, .ComponentSubOption{
            height: 40px;
            width: 40px;
            border-radius:40px;
            background-color: #FFFFFF;
            border:1px solid #707070;  
            font-size: 15px;
            color : #707070;
        }

        .ComponentSubOptionSelected, .ComponentSubOption:hover{
            background-color: #B6BEFD;
        }


        .ComponentParameters{
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            flex: 1;
            align-items: center;
            border-top: 4px solid #FFF;
            padding-top: 10px;     
        }

        .ComponentOptions{
            display:flex;
            flex-direction:column;
            justify-content:flex-start;
        }

        .ComponentSubOptions{
            display:flex;
            flex-direction:row;
            justify-content:space-between;
            width: 100%;
            padding: 5px;
        }
        
        div.output_subarea{
            padding:0px
        }
        
        .viewsTitle {
            display: flex;
            flex-direction: column;
            text-align: center;
            justify-content: center;
            font-size: 24px;   
            padding: 10px;

        }
        </style>
        <div id="parameter_''' + str(self.ref) + '''"></div>
        '''

        parameter_component_js = '''
        requirejs.config({
            paths: {
                'react': 'https://unpkg.com/react@16.8.6/umd/react.development',
                'react-dom': 'https://unpkg.com/react-dom@16/umd/react-dom.development'
            }
        });

        requirejs(['react', 'react-dom'], function(React, ReactDOM) {
            class Util {
                static create_UUID(){
                    var dt = new Date().getTime();
                    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
                        var r = (dt + Math.random()*16)%16 | 0;
                        dt = Math.floor(dt/16);
                        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
                    });
                    return uuid;
                }
            }

            class ParametersComponent extends React.Component {
                constructor(props) {
                    super(props)
                    let self = this;
                    this.state = { 
                        parameters:{
                            "options":{
                                "children":{},
                                "alt": "Settings",
                                "icon": "parameters/parameters.png",
                                "label" : "Customize parameters",
                                "action" : function(){ self.displayOptions() },
                            },
                            "textbook":{
                                "children":{},
                                "alt": "Text book",
                                "icon": "parameters/textbook.png",
                                "label" : "textbook cell",
                                "action" : function(){ self.displayTextBook() },
                            },
                            "unitcell":{
                                "children":{},
                                "alt": "Basis",
                                "icon": "parameters/unitcell.png",
                                "label" : "Unit cell",
                                "action" : function(){ self.displayUnitCell() },
                            },
                            "bravais":{
                                "children":{},
                                "alt": "Bravais",
                                "icon": "parameters/bravais.png",
                                "label" : "Bravais structure",
                                "action" : function(){ self.displayLattice() },
                            },
                            "miller":{
                                "children":{
                                    "100":{
                                        "icon": "parameters/miller100.png",
                                        "alt": "100",
                                        "label" : "Miller planes (100)",
                                        "action" : function(){ self.displayPlane1B() },
                                    },                        
                                    "010":{
                                        "icon": "parameters/miller010.png",
                                        "alt": "010",
                                        "label" : "Miller planes (010)",
                                        "action" : function(){ self.displayPlane2B() },
                                    },                        

                                    "001":{
                                        "icon": "parameters/miller001.png",
                                        "alt": "001",
                                        "label" : "Miller planes (001)",
                                        "action" : function(){ self.displayPlane3B() },
                                    },  
                                    //"111":{
                                    //   "icon": "parameters/miller111.png",
                                    //    "alt": "111",
                                    //    "label" : "Miller planes (111)",
                                    //    "action" : function(){ self.todo() },
                                    //},    
                                },
                                "icon": "parameters/miller.png",
                                "label" : "Miller planes",
                                "alt": "Miller plane",
                                "action" : function(){ },
                            },
                        }, 
                        selectedParameter:"textbook",
                        selectedOption:undefined,
                    } 
                }    

                todo(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedTest"]("TODO", "TODO");
                }

                displayOptions(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayOptions"]();
                }

                displayTextBook(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayTextBook"]();
                }
                
                displayUnitCell(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayUnitCell"]();
                }
                
                displayLattice(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayLattice"]();
                }

                displayPlane1A(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayPlane1A"]();
                }
                
                displayPlane1B(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayPlane1B"]();
                }
                
                displayPlane2A(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayPlane2A"]();
                }
                
                displayPlane2B(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayPlane2B"]();
                }
                
                displayPlane3A(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayPlane3A"]();
                }
                
                displayPlane3B(){
                    CrystalViewerSimplified_''' + str(self.ref) + '''["exposedDisplayPlane3B"]();
                }
                
                selectParameter(parameter){
                    this.setState({
                        selectedParameter:parameter, 
                        selectedOption:undefined,
                    })
                    //CrystalViewerSimplified_''' + str(self.ref) + '''["exposedTest"](parameter, "TODO")
                }

                selectOption(option){
                    this.setState({
                        selectedOption:option,
                    })
                    //CrystalViewerSimplified_''' + str(self.ref) + '''["exposedTest"](option, "TODO")
                }

                callOption(option){
                    this.selectOption(option)
                    var parameter = this.state.parameters[this.state.selectedParameter].children[option]
                    this.callbackParameter(parameter)
                }

                callbackParameter(parameter){
                   console.log(parameter)
                    if (parameter.action){
                       parameter.action() 
                    }
                }

                callParameter(param){
                    this.selectParameter(param)
                    var parameter = this.state.parameters[param]
                    this.callbackParameter(parameter)
                }



                render(){
                    var children = Array()    
                    var style = {
                        //backgroundSize: "50px 50px",
                        //backgroundImage: "url(" + crystal_instance.icon + ")",
                        display: "flex",
                        alignItems: "center",
                        flexDirection: "row",
                        justifyContent: "center",
                    }       
                    let self = this


                    
                    for (let parameter in this.state.parameters) {
                        let parameter_instance = this.state.parameters[parameter]
                        if (parameter != this.state.selectedParameter){
                            children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentOption", style:style, onClick:function(e){self.callParameter(parameter)}, title:parameter_instance.label}, parameter_instance.alt))
                        } else {
                            children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentOptionSelected", style:style, title:parameter_instance.label}, parameter_instance.alt))
                        }   
                        children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentOptionSpacer"}))
                        
                        if (parameter == this.state.selectedParameter){
                            var mat_children = Array()    
                            var opts = this.state.parameters[this.state.selectedParameter].children
                            for (let option in opts) {
                                let parameter_instance = opts[option]
                                if (option != this.state.selectedOption){
                                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentSubOption", style:style, onClick:function(e){self.callOption(option)}, title:parameter_instance.label}, parameter_instance.alt))
                                } else {
                                    mat_children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentSubOptionSelected", style:style, title:parameter_instance.label}, parameter_instance.alt))
                                }                                            
                            }    
                            if (mat_children.length > 0){
                                children.push(React.createElement("div", {key:Util.create_UUID(), className:"ComponentSubOptions"}, mat_children))
                            }
                        }
                    }  

                    var components = React.createElement("div", {key:Util.create_UUID(), className:"ComponentParameters"}, children)

                    var opt = React.createElement("div", {key:Util.create_UUID(), className:"", style:{display:"flex", flexDirection:"row", backgroundColor:'#EEEEEE', justifyContent:'flex-start', height:'700px', width:'140px', borderRight:'4px solid #FFF'}}, [components])
                    var views = React.createElement("div", {key:Util.create_UUID(), className:"viewsTitle"}, "Views")
                    var div = React.createElement("div", {key:Util.create_UUID(), className:"", style:{display:"flex", flexDirection:"column", backgroundColor:'#EEEEEE', justifyContent:'flex-start', height:'700px'}}, [opt])
                    return div
                }
            }

            ReactDOM.render(
                React.createElement(ParametersComponent, {}),
                document.getElementById("parameter_''' + str(self.ref) + '''")
            );
        });
        '''      
        return parameter_component_view, parameter_component_js;

        
    def displayFrame(self):
        crystal_component_view, crystal_component_js = self.buildCrystal()
        parameter_component_view, parameter_component_js = self.buildParameters()
        
        with self.crystal_component_output:
            display(HTML(crystal_component_view))
            display(Javascript(crystal_component_js)) 
    
        with self.parameters_component_output:
            display(HTML(parameter_component_view))
            display(Javascript(parameter_component_js)) 
          
    def exposedTest(self, value1, value2):
        with self.content_component_output:
            display("Value1 = " , value1)
            display("Value2 = " , value2)
            
    def buildInterfaceJS(self):
        interface_js = "<script type='text/Javascript'>\n";
        refobj = "CrystalViewerSimplified_" + str(self.ref)
        interface_js += "var " + refobj + " = {};\n";
        for method in inspect.getmembers(self, predicate=inspect.ismethod):
            if (method[0].startswith("exposed")):
                interface_js += refobj + "['" + method[0] + "'] = function ("
                for i, parameter in enumerate (inspect.signature(method[1]).parameters):
                    if (i==0):
                        interface_js += parameter
                    else:
                        interface_js += ", " + parameter
                interface_js += "){\n";
                interface_js += "    var command = 'from nanohubtools import CrystalViewerSimplified ; CrystalViewerSimplified.find_instance("+ str(self.ref) + ")." + method[0] +"(";
                for i, parameter in enumerate (inspect.signature(method[1]).parameters):
                    if (i==0):
                        interface_js += "\\'' + String(" + parameter + ") + '\\'"
                    else:
                        interface_js += ", \\'' + String(" + parameter + ") + '\\'"
                interface_js += ")';\n";
                interface_js += "    console.log('Executing Command: ' + command);\n"
                interface_js += "    var kernel = IPython.notebook.kernel;\n"
                interface_js += "    kernel.execute(command);\n"
                interface_js += "}\n";
        interface_js+='</script>\n'
        return interface_js
    
    def refreshView(self):
        if (self.current_view == "options"):
            self.exposedDisplayOptions()
        elif (self.current_view == "textbook"):
            self.exposedDisplayTextBook()
        elif (self.current_view == "unitcell"):
            self.exposedDisplayUnitCell()
        elif (self.current_view == "lattice"):
            self.exposedDisplayLattice()
        elif (self.current_view == "plane1A"):
            self.exposedDisplayPlane1A()
        elif (self.current_view == "plane1B"):
            self.exposedDisplayPlane1B()
        elif (self.current_view == "plane2A"):
            self.exposedDisplayPlane2A()
        elif (self.current_view == "plane2B"):
            self.exposedDisplayPlane2B()
        elif (self.current_view == "plane3A"):
            self.exposedDisplayPlane3A()
        elif (self.current_view == "plane3B"):
            self.exposedDisplayPlane3B()


    def displayWindow(self):   
        self.displayFrame()
        display(HTML(self.buildInterfaceJS()))
        with self.window:
            clear_output()
            #display(self.options_cont)
            display(VBox([                
                self.crystal_component_output,
                HBox([
                    self.parameters_component_output,
                    self.content_component_output
                ], layout=Layout(flex='1', height="100%"))
            ], layout=Layout(flexDirection="row", width="100%", height="700px")))
            
            
                
    def displayOptions(self):
        container_structure = VBox(layout=Layout(width='100%', height='100%'))
        children_structure = []
        for p in self.parameters_structure :
            if p in self.options:            
                children_structure.append(self.options[p])
            else:
                children_structure.append(Button(description=p.replace('_',''),layout=Layout(width='auto'),style=ButtonStyle(button_color='lightblue')))

                               
        self.options['Crystal_structure'].dd.observe(lambda b, this=self : this.showMaterial(int(b['new'])), 'value')

        self.options['Draw_miller_plane'].value = "yes"
        self.options['Draw_plane_1'].value = "yes"
        self.options['Miller_index_1_1'].value = 1
        self.options['Miller_index_1_2'].value = 0
        self.options['Miller_index_1_3'].value = 0
        self.options['Draw_plane_2'].value = "yes"
        self.options['Miller_index_2_1'].value = 0
        self.options['Miller_index_2_2'].value = 1
        self.options['Miller_index_2_3'].value = 0
        self.options['Draw_plane_3'].value = "yes"
        self.options['Miller_index_3_1'].value = 0
        self.options['Miller_index_3_2'].value = 0
        self.options['Miller_index_3_3'].value = 1
        
        container_structure.children = children_structure
        container_miller = self.displayMillerOptions()
        self.showMaterial(1)
        self.options_cont.children = [container_structure]
        self.getCache()
        self.refreshView()
        
        
    def getCurrentParameters(self):
        parameters = {}
        
        for ii in [str(i) for i in range(1,13)]:
            if (ii != self.options["Crystal_structure"].value):
                self.options[ii].value == self.options[ii].dd.options[0]      
        for key, val in self.options.items():
            units = ''
            if key in self.parameters and self.parameters[key]['units'] is not None:
                units = str(self.parameters[key]['units'])
            parameters[key] = str(val.value) + units
        return parameters;
    

    def getCache(self):
        parameters = self.getCurrentParameters()
        hashstr =  json.dumps(parameters, sort_keys=True).encode()
        
        hashitem = hashlib.sha1(hashstr).hexdigest()
        if self.hashitem != hashitem:
            xml = None
            if hashitem in self.hashtable:
                with self.content_component_output:
                    clear_output()  
                    print("LOADING CACHE ...." + hashitem)
                with open(self.hashtable[hashitem],'rt' ) as f:
                    xml = f.read()
            else:
                if os.path.isfile(hashitem + ".xml"):
                    with self.content_component_output:
                        clear_output()  
                        print("REBUILD CACHE ...." + hashitem)
                    driver_json = self.generateDriver( {'parameters':parameters } )
                    session_id = self.session.getSession(driver_json)
                    with open(hashitem + ".xml",'rt' ) as f:
                        xml = f.read()
                    self.hashtable[hashitem] = hashitem + ".xml"
                        
                else:                
                    with self.content_component_output:
                        clear_output()  
                        print("GENERATING CACHE ...." + hashitem)
                    driver_json = self.generateDriver( {'parameters':parameters } )
                    session_id = self.session.getSession(driver_json)
                    with self.content_component_output:            
                        print ("new", hashitem, session_id)
                        status = self.session.checkStatus(session_id) 
                        loading = True
                        while loading == True:
                            if 'success' in status and status['success'] and 'finished' in status and status['finished'] and status['run_file'] != "":
                                loading = False
                            else:    
                                print ("Running ", session_id)
                                time.sleep(5);
                                status = self.session.checkStatus(session_id) 
                    xml = self.session.getResults(session_id, status['run_file'])
                    self.hashtable[hashitem] = hashitem + ".xml"
                    with open(self.hashtable[hashitem],'wt' ) as f:
                        f.write(xml)
                    
            xml = ET.fromstring(xml)
            results = xml.find('output')
            drawings = results.findall('drawing')
            self.textbook = None;
            self.lattice = None;
            self.unitcell = None;
            self.plane1A = None;
            self.plane1B = None;
            self.plane2A = None;
            self.plane2B = None;
            self.plane3A = None;
            self.plane3B = None;
            for drawing in drawings:
                if 'id' in drawing.attrib:
                    text = drawing.attrib['id']#self.getText(drawing, ['about', 'label'])
                else:
                    text = ""
                if text == "structure1":  #"Basis":
                    self.unitcell = drawing
                elif text == "structure2":  #"Lattice grid":
                    self.lattice = drawing
                elif text == "structure0":  #:"Text book unit cell":
                    self.textbook = drawing
                elif text == "plane1_side_A": #:"Crystal on one side of plane 1"
                    self.plane1A = drawing
                elif text == "plane1_side_B": #:"Crystal on the other side of plane 1"
                    self.plane1B = drawing
                elif text == "plane2_side_A": #:"Crystal on one side of plane 2"
                    self.plane2A = drawing
                elif text == "plane2_side_B": #:"Crystal on the other side of plane 2"
                    self.plane2B = drawing
                elif text == "plane3_side_A": #:"Crystal on one side of plane 3"
                    self.plane3A = drawing
                elif text == "plane3_side_B": #:"Crystal on the other side of plane 3"
                    self.plane3B = drawing
            if self.textbook == None:
                self.textbook = self.unitcell
            if self.lattice == None:
                self.lattice = self.unitcell
        with self.content_component_output:
            clear_output()  
        self.hashitem = hashitem
            
    def exposedDisplayOptions(self):
        self.getCache()
        self.current_view = "options"
        with self.content_component_output:
            clear_output()
            display(self.options_cont)
     
    def exposedDisplayTextBook(self):
        self.getCache()        
        self.current_view = "textbook"
        if self.textbook != None:
            self.plotDrawing(self.textbook,self.content_component_output)
    
    def exposedDisplayUnitCell(self):
        self.getCache()        
        self.current_view = "unitcell"
        if self.unitcell != None:
            self.plotDrawing(self.unitcell,self.content_component_output)

    def exposedDisplayLattice(self):
        self.getCache()        
        self.current_view = "lattice"
        if self.lattice != None:
            self.plotDrawing(self.lattice,self.content_component_output)

    def exposedDisplayPlane1A(self):
        self.displayPlane("plane1A", self.plane1A)
        
    def exposedDisplayPlane1B(self):
        self.displayPlane("plane1B", self.plane1B)
        
    def exposedDisplayPlane2A(self):
        self.displayPlane("plane2A", self.plane2A)
        
    def exposedDisplayPlane2B(self):
        self.displayPlane("plane2B", self.plane2B)
        
    def exposedDisplayPlane3A(self):
        self.displayPlane("plane3A", self.plane3A)
        
    def exposedDisplayPlane3B(self):
        self.displayPlane("plane3B", self.plane3B)
        
    def displayPlane(self, plane, content):
        self.getCache()
        self.current_view = plane
        if content != None:
            self.plotDrawing(content,self.content_component_output)

    def exposedSelectCrystal(self, crystal):
        if (self.options["Crystal_structure"].value != crystal):
            self.options["Crystal_structure"].value = crystal;
            self.getCache()
            self.refreshView()

    def exposedSelectMaterial(self, crystal, material):
        if (self.options["Crystal_structure"].value != crystal or self.options[crystal].value != material):
            self.options["Crystal_structure"].value = crystal;
            self.options[crystal].value = material;
            self.getCache()
            self.refreshView()

    def plotDrawingPlotly(self, draw, out):
        label = self.getText(draw, ["index", "label"])
        if out == None:
            out = Floatview(title=label, mode = 'split-bottom')
        self.fig.data = []
        #out.clear_output()     
        traces = []
        molecules = draw.findall('molecule')
        for molecule in molecules:
            atoms, connections = self.getMolecule(molecule)        

            xt = None
            yt = None
            zt = None
            st = None
            color = {}
            colorset = set()
            for id, atom in atoms.items():
                colorset.add(atom[3])
            colorset = list(colorset)
        
            xt = {}
            yt = {}
            zt = {}
            st = {}

            for id, atom in atoms.items():
                if atom[5] == "enabled" and (atom[3] not in ["He","Yb","Xe","Zn"]):
                    xv = (self.xt + atom[0]).tolist()
                    yv = (self.yt + atom[1]).tolist()
                    zv = (self.zt + atom[2]).tolist()
                    xv.extend([[point for point in xv[0]],[point for point in xv[1]],[]])
                    yv.extend([[point for point in yv[0]],[point for point in yv[1]],[]])
                    zv.extend([[point for point in zv[0]],[point for point in zv[1]],[]]) 
                    if atom[3] in xt:
                        xt[atom[3]].extend(xv)
                        yt[atom[3]].extend(yv)
                        zt[atom[3]].extend(zv) 
                    else :
                        xt[atom[3]] = xv
                        yt[atom[3]] = yv
                        zt[atom[3]] = zv
                        
            for atom in list(xt.keys()):
                
                colorscalea = [[0,self.jcpk[atom]], [1,self.jcpk[atom]]]

                self.fig.add_surface(
                    x = xt[atom], 
                    y = yt[atom], 
                    z = zt[atom], 
                    hovertext = atom,
                    showscale = False,
                    hoverinfo = "text",
                    colorscale = colorscalea,
                    connectgaps = False,
                    lighting = { 
                        'specular' : 1 ,
                        'ambient' : 0.4,
                        'diffuse' :0.5, 
                        'roughness' : 0.9, 
                        'fresnel' : 2.0,
                    }
                )
                   
            
            xt = {}
            yt = {}
            zt = {}
            st = {}
            for c in colorset:
               xt[c]=[]
               yt[c]=[]
               zt[c]=[]
               st[c]=[]
               
            for atom1, connection in connections.items():
                for atom2 in connection:
                    at1 = atom1
                    at2 = atom2
                    u = np.array([atoms[at2][i]-atoms[at1][i] for i in range(3)])        
                    u /= np.linalg.norm(u)
                    v1 = np.random.randn(3)  
                    v1 -= v1.dot(u) * u       
                    v1 /= np.linalg.norm(v1)
                    v2 = np.cross(v1, u)
                    v2 /= np.linalg.norm(v2)
                    sample = int(self.samples/2)
                    xd = np.linspace(atoms[at2][0], atoms[at1][0], sample, endpoint=True)
                    yd = np.linspace(atoms[at2][1], atoms[at1][1], sample, endpoint=True)
                    zd = np.linspace(atoms[at2][2], atoms[at1][2], sample, endpoint=True)
                    atm1 = atoms[at1][3]
                    if atm1 == "He":
                        atm1 = atoms[at2][3]
                    atm2 = atoms[at2][3]
                    if atm1 != atm2:
                        for i in range(0,int(sample/2)+2):
                            xt[atm2].append((self.cosphi*v1[0] + self.sinphi*v2[0] + xd[i]).tolist())
                            yt[atm2].append((self.cosphi*v1[1] + self.sinphi*v2[1] + yd[i]).tolist())
                            zt[atm2].append((self.cosphi*v1[2] + self.sinphi*v2[2] + zd[i]).tolist())
                        xt[atm2].append([])
                        zt[atm2].append([])
                        yt[atm2].append([])
                        
                        for i in range(int(sample/2)-1, sample):
                            xt[atm1].append((self.cosphi*v1[0] + self.sinphi*v2[0] + xd[i]).tolist())
                            yt[atm1].append((self.cosphi*v1[1] + self.sinphi*v2[1] + yd[i]).tolist())
                            zt[atm1].append((self.cosphi*v1[2] + self.sinphi*v2[2] + zd[i]).tolist())
                        xt[atm1].append([])
                        zt[atm1].append([])
                        yt[atm1].append([])
                    else:
                        for i in range(sample):
                            xt[atm1].append((self.cosphi*v1[0] + self.sinphi*v2[0] + xd[i]).tolist())
                            yt[atm1].append((self.cosphi*v1[1] + self.sinphi*v2[1] + yd[i]).tolist())
                            zt[atm1].append((self.cosphi*v1[2] + self.sinphi*v2[2] + zd[i]).tolist())
                        xt[atm1].append([])
                        zt[atm1].append([])
                        yt[atm1].append([])
                   
            for c in colorset:    
                opacity = 1.0
                if c == "He":
                    opacity = 0.2
                self.fig.add_surface(
                    x = xt[c], 
                    y = yt[c], 
                    z = zt[c], 
                    hovertext = '',    
                    showscale = False,
                    hoverinfo = 'text',
                    colorscale = [[0,self.jcpk[c]], [1,self.jcpk[c]]],
                    connectgaps = False,
                    opacity = opacity
                )
                
            polys = self.getPolygons(draw);

            for points in polys:
                xt = [point[0] for point in points]
                yt = [point[1] for point in points]
                zt = [point[2] for point in points]

                delaunayaxis = None
                if len(set(xt)) == 1 : 
                    delaunayaxis = 'x'
                elif len(set(yt)) == 1 : 
                    delaunayaxis = 'y'
                elif len(set(zt)) == 1 : 
                    delaunayaxis = 'z'

                self.fig.add_mesh3d(
                    x = xt, 
                    y = yt, 
                    z = zt, 
                    color = 'lightgrey',
                    hovertext = '',
                    hoverinfo = 'text',
                    delaunayaxis = delaunayaxis
                )

        with out:   
            display(self.fig)
            
        return self.fig   


        
    def plotDrawing(self, draw, out):
        if self.engine == "three":
            return self.plotDrawingThree(draw, out)
        else :
            return self.plotDrawingPlotly(draw, out)
            
    def plotDrawingThree(self, draw, out):
        label = self.getText(draw, ["index", "label"])
        if out == None:
            out = Floatview(title=label, mode = 'split-bottom')
        self.fig.data = []
        traces = []
        molecules = draw.findall('molecule')
        balls = []
        geometry = pt.SphereGeometry(radius=.5, widthSegments=16, heightSegments=16)
        for molecule in molecules:    
            atoms, connections = self.getMolecule(molecule)
                        
            xt = None
            yt = None
            zt = None
            st = None
            color = {}
            colorset = set()
            for id, atom in atoms.items():
                colorset.add(atom[3])
            colorset = list(colorset)
        

            for id, atom in atoms.items():
                if atom[5] == "enabled" and (atom[3] not in ["He","Yb","Xe","Zn"]):
                    balls.append(pt.Mesh(
                        geometry = geometry, 
                        material = pt.MeshLambertMaterial(color=self.jcpk[atom[3]], reflectivity=0.1),
                        position = [atom[0], atom[1], atom[2]] 
                    ))
                    
               
            for atom1, connection in connections.items():
                for atom2 in connection:
                    at1 = atoms[atom1]
                    at2 = atoms[atom2]
                    c1 = at1[3]
                    c2 = at2[3]
                    if c1 == "He":
                        c1 = c2
                    opacity = 1.0
                    linewidth = 10
                    if c1 == c2:
                        if c1 == "He":
                            opacity = 0.1
                            linewidth = 5
                        balls.append(pt.LineSegments2(
                            geometry = pt.LineSegmentsGeometry(
                                positions = [
                                    [ [at1[0],at1[1],at1[2]], [at2[0],at2[1],at2[2]] ],
                                ]
                            ), 
                            material = pt.LineMaterial(color=self.jcpk[c1], linewidth=linewidth, opacity=opacity, transparent=True),
                        ))
                    else:
                        balls.append(pt.LineSegments2(
                            geometry = pt.LineSegmentsGeometry(
                                positions = [
                                    [ [at1[0],at1[1],at1[2]], [(at2[0]+at1[0])/2,(at2[1]+at1[1])/2,(at2[2]+at1[2])/2] ],
                                ]
                            ), 
                            material = pt.LineMaterial(color=self.jcpk[c1], linewidth=linewidth, opacity=opacity, transparent=True),
                        ))
                        balls.append(pt.LineSegments2(
                            geometry = pt.LineSegmentsGeometry(
                                positions = [
                                    [ [(at2[0]+at1[0])/2,(at2[1]+at1[1])/2,(at2[2]+at1[2])/2], [at2[0],at2[1],at2[2]] ],
                                ]
                            ), 
                            material = pt.LineMaterial(color=self.jcpk[c2], linewidth=linewidth, opacity=opacity, transparent=True),
                        ))
                   

            polys = self.getPolygons(draw);

            for points in polys:
            
                p1 = np.array(points[0])
                p2 = np.array(points[1])
                p3 = np.array(points[2])

                v1 = p3 - p1
                v2 = p2 - p1
                
                cp = np.cross(v1, v2)
                
                avgx = sum([points[i][0] for i in range(3)])/3
                avgy = sum([points[i][1] for i in range(3)])/3
                avgz = sum([points[i][2] for i in range(3)])/3
                
                mesh = pt.Mesh(
                    geometry = pt.PlaneGeometry(
                        width=20,
                        height=20,
                        widthSegments=10,
                        heightSegments=10,
                    ), 
                    material = pt.MeshLambertMaterial(color='#EEEEEE', reflectivity=0.1, side='DoubleSide'),
                    position = [avgx, avgy, avgz],
                )
                
                mesh.lookAt([cp[0],cp[1],cp[2]])
                balls.append(mesh)
   
                
        c = pt.PerspectiveCamera(
            position=[0, 10, 10], 
            up=[0, 1, 0],
            children=[pt.DirectionalLight(color='white', position=[3, 5, 1], intensity=0.5)], 
            aspect = 800/600,
        )
        balls.append(c)
        balls.append(pt.AmbientLight(color='#777777'))
        with out:   
            scene = pt.Scene(children=balls)
            renderer = pt.Renderer(camera=c, 
                scene=scene, 
                controls=[pt.OrbitControls(controlling=c)],
                width = 800,
                height = 600,
                antialias=False,
            )
            display(renderer)
            
        return renderer