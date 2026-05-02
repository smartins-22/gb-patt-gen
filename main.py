import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import math
import os
import json
import re

###########################################################################################################
####
####                                   Grid-Based Pattern Generator
####
###########################################################################################################

VERSION="3.7"

LANGUAGES = {
    'fr': {
        'main_title': "Générateur de Motif v{} | {}",
        'default_collection_name': "Ma Collection",
        'default_pattern_name' : "Motif",
        'rename_collection' : "Renommer la collection",
        'rename_pattern' : "Renommer",
        'copy_pattern' : "Copier",
        'apply_selection' : "Applique à la selection",
        'import_json' : "Import Collection (JSON)",
        'export_json' : "Export Collection (JSON)",
        'batch_svg_export' : "Générer la Collection (SVG)",
        'label_grid' : "GRILLE",
        'grid_orthogonal': "Orthogonale",
        'grid_isometric': "Isométrique",
        'apply_grid' : "Appliquer",
        'fill_all' : "Remplir la grille",
        'fill_options' : "Option de remplissage",
        'fill_free': "Libre",
        'fill_occupied': "Occupé",
        'fill_loop': "Boucle",
        'fill_style_plain': "Plein",
        'fill_style_outline': "Contour",
        'fill_style_void': "Vide",
        'erase_all' : "Effacer Tout",
        'label_tools' : "OUTILS",
        'tool_shapes': "Formes",
        'shape_circle': "⬤ Cercle",
        'shape_square': "⬛ Carré",
        'tool_drawing' : "Dessin",
        'label_param' : "PARAMETRES",
        'btn_outline_on' : "CONTOUR",
        'btn_outline_off' : "PLEIN",
        'btn_neg_on' : "NEGATIF",
        'btn_neg_off' : "POSITIF",
        'shape_size' : "Taille Forme",
        'outline_width': "Contour (%)",
        'lines_width' : "Epaisseur trait",
        'index_ratio' : "Taille Index",
        'label_options' : "OPTIONS",
        'show_grid':  "Afficher la grille",
        'show_lines': "Afficher le dessin",
        'show_shapes': "Afficher les formes",
        'crop_grid' : "Rogner à la grille",
        'add_index' : "Ajouter Index",
        'pos_left': "►|  Gauche",
        'pos_centred': "◄|► Centré",
        'pos_right': " |► Droite",
        'pos_edge': "►⬚  Bord",
        'gen_svg':"Générer le Motif (SVG)",
        'rename_coll_title' : "Collection",
        'rename_coll_txt' : "Nouveau nom de collection :",
        'apply_to_sel_confirm_title':"Appliquer ?",
        'apply_to_sel_confirm_txt':"Appliquer la configuration en cours aux motifs sélectionnés ?",
        'apply_to_sel_done_title':"Fait",
        'apply_to_sel_done_txt':"Mise à jour des motifs effectuée !",
        'export_done_title' : "Fait",
        'export_done_txt' : "Export des fichiers SVG terminé !",
        'new_patt_title' : "Nouveau Motif",
        'new_patt_txt' : "Entrez le nom du motif :",
        'error' : 'Erreur',
        'err_exists' : "Ce nom existe déjà !",
        'rename_patt_title' : "Renommer Motif",
        'rename_patt_txt' :"Nouveau nom pour ce motif :",
        'copy_patt_title' :"Copier",
        'copy_patt_txt' : "Nom de la copie :",
        'del_patt_confirm_title' : "Supprime ?",
        'del_patt_confirm_txt' : "Êtes-vous sûr de vouloir supprimer définitivement\nle motif '{}' ?",
        'del_multi_patt_confirm_title' : "Supprimer ?",
        'del_multi_patt_confirm_txt' : "Êtes-vous sûr de vouloir supprimer définitivement\ntous les motifs sélectionnés ({})?",
        'btn_yes' : "Oui",
        'btn_no' : "Non",
        'btn_ok' : "OK",
        'btn_cancel' : "Annuler",
        'warning': "Attention",
        'import_confirm_title' : "Confirmation de l'import",
        'import_confirm_txt':"L'importation va écraser la collection en cours.\nÊtes-vous sûr de vouloir continuer ?",
        'err_invalid_input' : "Entrée invalide",
        'clear_all_confirm_title' : "Effacer ?",
        'clear_all_confirm_txt' : "Effacer le canvas en cours ?\n",
        'resize_confirm_title' : "Redimensionner ?",
        'resize_confirm_txt' : "Redimensionner la grille va supprimer les éléments en dehors de la nouvelle grille.\nContinuer ?",
        'close_confirm_title': "Quitter",
        'close_confirm_txt': "Voulez-vous vraiment fermer l'application ?",
        'label_transform': "TRANSFORMER",
        'transform_scale': "Redimensionner",
        'transform_shift': "Translater",
        'transform_copy_shift': "Copier & Translater",
        'transform_symmetry': "Symétrie",
        'dim_x': "X (Colonnes)",
        'axis_x': "X (Horizontal)",
        'dim_y': "Y (Lignes)",
        'axis_y': "Y (Vertical)",
        'op_multiply': "Multiplier",
        'op_divide': "Diviser",
        'scale_title': "Redimensionner le Motif",
        'scale_dim_prompt': "Sélectionnez la dimension à transformer :",
        'scale_op_prompt': "Opération :",
        'scale_factor_prompt': "Facteur de redimensionnement (nombre entier) :",
        'scale_confirm_title': "Redimensionner ?",
        'scale_confirm_txt': "La transformation va supprimer toutes les formes.\nContinuer ?",
        'shift_title': "Translater le Motif",
        'shift_dim_prompt': "Sélectionnez la dimension de translation :",
        'shift_step_prompt': "Pas du décalage (nombre entier) :",
        'shift_confirm_title': "Translater ?",
        'shift_confirm_txt': "La translation peut supprimer les éléments en dehors de la grille.\nContinuer ?",
        'copy_shift_title': "Copier & Translater le Motif",
        'copy_shift_dim_prompt': "Sélectionnez la dimension de copie & translation :",
        'symmetry_title': "Symétrie du Motif",
        'symmetry_dim_prompt': "Sélectionnez l'axe de symétrie :",
        'err_value_too_small': "La valeur '{0}' est trop petite pour la dimension {1} (min : {2}).",
        'err_value_too_large': "La valeur '{0}' est trop grande pour la dimension {1} (max : {2}).",
        'err_factor_too_large': "Le facteur '{0}' est trop grand pour la dimension {1} (max : {2}).",
        'transform_done': "Transformation terminée !",
        'filling_done': "Remplissage terminé !"
    },
    'en': {
        'main_title': "Pattern Generator v{} | {}",
        'default_collection_name': "My Collection",
        'default_pattern_name' : "Pattern",
        'rename_collection' : "Rename collection",
        'rename_pattern' : "Rename",
        'copy_pattern' : "Copy",
        'apply_selection' : "Apply to the selection",
        'import_json' : "Import Collection (JSON)",
        'export_json' : "Export Collection (JSON)",
        'batch_svg_export' : "Generate Collection (SVG)",
        'label_grid' : "GRID",
        'grid_orthogonal': "Orthogonal",
        'grid_isometric': "Isometric",
        'apply_grid' : "Apply",
        'fill_all' : "Fill the grid",
        'fill_options' : "Filling options",
        'fill_free': "Free",
        'fill_occupied': "Occupied",
        'fill_loop': "Loop",
        'fill_style_plain': "Plain",
        'fill_style_outline': "Outlined",
        'fill_style_void': "Void",
        'erase_all' : "Erase all",
        'label_tools' : "TOOLS",
        'tool_shapes': "Shapes",
        'shape_circle': "⬤ Circle",
        'shape_square': "⬛ Square",
        'tool_drawing' : "Drawing",
        'label_param' : "PARAMETER",
        'btn_outline_on' : "OUTLINED",
        'btn_outline_off' : "FILLED",
        'btn_neg_on' : "NEGATIVE",
        'btn_neg_off' : "POSITIVE",
        'shape_size' : "Shape size",
        'outline_width': "Outl. width (%)",
        'lines_width' : "Line thickness",
        'index_ratio' : "Index size",
        'label_options' : "OPTIONS",
        'show_grid':  "Show the grid",
        'show_lines': "Show the drawing",
        'show_shapes': "Show the shapes",
        'crop_grid' : "Crop to the grid",
        'add_index' : "Add Index",
        'pos_left': "►|  Left",
        'pos_centred': "◄|► Centered",
        'pos_right': " |► Right",
        'pos_edge': "►⬚  Edge",
        'gen_svg':"Generate Pattern (SVG)",
        'rename_coll_title' : "Collection",
        'rename_coll_txt' : "New name of the collection:",
        'apply_to_sel_confirm_title':"Apply ?",
        'apply_to_sel_confirm_txt':"Apply the currrent configuration to the selected patterns?",
        'apply_to_sel_done_title':"Done",
        'apply_to_sel_done_txt':"Update of patterns done!",
        'export_done_title' : "Done",
        'export_done_txt' : "Export of SVG files done!",
        'new_patt_title' : "New Pattern",
        'new_patt_txt' : "Enter new pattern name:",
        'error' : 'Error',
        'err_exists' : "This name already exists!",
        'rename_patt_title' : "Rename Pattern",
        'rename_patt_txt' :"New name for this pattern:",
        'copy_patt_title' :"Copy",
        'copy_patt_txt' : "Name of the copy:",
        'del_patt_confirm_title' : "Delete?",
        'del_patt_confirm_txt' : "Are you sure you want to delete\nthe pattern '{}'?",
        'del_multi_patt_confirm_title' : "Delete?",
        'del_multi_patt_confirm_txt' : "Are you sure you want to delete\nall the selected patterns ({})?",
        'btn_yes' : "Yes",
        'btn_no' : "No",
        'btn_ok' : "OK",
        'btn_cancel' : "Cancel",
        'warning': "Warning",
        'import_confirm_title' : "Import?",
        'import_confirm_txt':"The Import will overwrite current collection.\nContinue?",
        'err_invalid_input' : "Invalid input",
        'clear_all_confirm_title' : "Clear ?",
        'clear_all_confirm_txt' : "Clear the canvas ?\n",
        'resize_confirm_title' : "Resize ?",
        'resize_confirm_txt' : "Resizing the grid will delete elements outside the new grid.\nContinue ?",
        'close_confirm_title': "Quit",
        'close_confirm_txt': "Do you really want to close the application?",
        'label_transform': "TRANSFORM",
        'transform_scale': "Scale",
        'transform_shift': "Shift",
        'transform_copy_shift': "Copy & Shift",
        'transform_symmetry': "Symmetry",
        'dim_x': "X (Columns)",
        'axis_x': "X (Horizontal)",
        'dim_y': "Y (Rows)",
        'axis_y': "Y (Vertical)",
        'op_multiply': "Multiply",
        'op_divide': "Divide",
        'scale_title': "Scale Pattern",
        'scale_dim_prompt': "Select dimension to scale:",
        'scale_op_prompt': "Operation:",
        'scale_factor_prompt': "Scale factor (must be integer):",
        'scale_confirm_title': "Scale Pattern?",
        'scale_confirm_txt': "Scaling will remove all shapes.\nContinue?",
        'shift_title': "Shift Pattern",
        'shift_dim_prompt': "Select dimension to shift:",
        'shift_step_prompt': "Shift step (integer):",
        'shift_confirm_title': "Shift Pattern?",
        'shift_confirm_txt': "Shifting may remove elements outside the grid.\nContinue?",
        'copy_shift_title': "Copy & Shift Pattern",
        'copy_shift_dim_prompt': "Select dimension to copy & shift:",
        'symmetry_title': "Mirror Pattern",
        'symmetry_dim_prompt': "Select axis of symmetry:",
        'err_value_too_small': "Value '{0}' is too small for dimension {1} (min : {2}).",
        'err_value_too_large': "Value '{0}' is too large for dimension {1} (max : {2}).",
        'err_factor_too_large': "Factor '{0}' is too large for the selected dimension {1} (max : {2}).",
        'transform_done': "Transformation complete!",
        'filling_done': "Filling complete!"
    }
}

 ###--------------------------------------------------------------------------------------------------------
 ###  SVGEditor
 ###--------------------------------------------------------------------------------------------------------
class SVGEditor:
    #--------------------------------------------------------------------------------------------------------
    #  _init_
    #--------------------------------------------------------------------------------------------------------
    def __init__(self, root):
        
        self.lang = "en"  # Default language
  
        self.root = root
        # --- Main window title handling
        #  - Using a StringVar attaching a function to update the window title automatically
        self.title_var = tk.StringVar()
        self.title_var.trace_add("write", lambda *args: self.root.title(self.title_var.get()))
        self.title_var.set(self.tr("main_title").format(VERSION,""))
       
        # --- State variables ---
        self.cols, self.rows = 4, 4
        self.padding = 90
        self.grid_type = tk.StringVar(value="orthogonal")

        self.show_grid = tk.BooleanVar(value=True)
        self.show_lines = tk.BooleanVar(value=True)
        self.show_shapes = tk.BooleanVar(value=True)
        self.crop_to_grid = tk.BooleanVar(value=True)
        self.negative_mode = tk.BooleanVar(value=False)
        self.fill_mode = tk.StringVar(value="A")
        self.use_outlined_shape = tk.BooleanVar(value=True)
        
        # -- Fill styles for each node type (free, occupied, loop)
        self.fill_styles_available = ["plain", "outline", "void"]
        self.current_fill_style_free = "plain"
        self.current_fill_style_occupied = "void"
        self.current_fill_style_loop = "outline"
        self.fill_style_free = tk.StringVar()
        self.fill_style_occupied = tk.StringVar()
        self.fill_style_loop = tk.StringVar()


        # -- Tool settings
        self.active_tool = tk.StringVar(value="line")
        self.current_shape_id = "circle"
        self.shapes_available = ["circle", "square"]
        self.shape_display_var = tk.StringVar() 
        self.line_start_point = None 
        self.shape_size_ratio = tk.DoubleVar(value=1.0)
        self.shape_stroke_pct = tk.IntVar(value=50) 
        self.line_stroke_width = tk.IntVar(value=10)
        self.color_shapes = "#000000" 
        self.color_lines = "#FF4500"

        self.pattern_shapes = {}   # Dict of shapes
        self.pattern_lines = set() # List of lines
        self.blocked_nodes = set() # List of blocked_nodes

        # -- Index setting
        self.show_index = tk.BooleanVar(value=False)
        self.index_pos_available = ["left", "centred", "right", "edge"]
        self.current_index_pos_id = "centred"
        self.index_pos_var = tk.StringVar()
        self.index_ratio = tk.DoubleVar(value=0.25)
        self.color_index = "#000000"

        # --- Collection's Data ---
        self.collection_name = self.tr("default_collection_name")
        self.order = [self.tr("default_pattern_name")+" 1"]  # List to manage the order of items
        self.collection = {self.tr("default_pattern_name") + " 1": self._get_blank_state()}
        self.current_pattern_name = self.tr("default_pattern_name")+" 1"

        # --- Initialize and configure UI ---
        self.setup_ui()
        self.load_pattern_from_collection(self.current_pattern_name)
        self.active_tool.set("line")
        self.canvas.bind("<Configure>", lambda e: self.draw_canvas())
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self._bind_shortcuts()
    #--------------------------------------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------------------------------------
    #  UI Setup
    #--------------------------------------------------------------------------------------------------------
    def setup_ui(self):
        # ---------------------------------
        # --          LEFT PANEL         --
        # --   Collection Management     --
        # ---------------------------------       
        self.left_panel = tk.Frame(self.root, width=260, bg="#dfe6e9", padx=10, pady=10)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)
        self.left_panel.pack_propagate(False)
        
        # Name of the collection
        self.lbl_coll_name = tk.Label(self.left_panel, text=self.collection_name, font=('Arial', 12, 'bold'), bg="#dfe6e9")
        self.lbl_coll_name.pack(pady=2)
        self.txt_rename_coll=tk.StringVar(value=self.tr('rename_collection'))
        tk.Button(self.left_panel, textvariable=self.txt_rename_coll, command=self.rename_collection, font=('Arial', 8)).pack(pady=(0,10))

        # List of patterns
        self.listbox = tk.Listbox(self.left_panel, selectmode=tk.EXTENDED, font=('Arial', 9))
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.on_list_select)
        self.listbox.bind('<F2>', self._on_listbox_rename_key)
        self.listbox.bind('<Delete>', self._on_listbox_delete_key)
        self.listbox.bind('<BackSpace>', self._on_listbox_delete_key)
        self.listbox.bind('<Shift-Up>', self._on_listbox_move_up)
        self.listbox.bind('<Shift-Down>', self._on_listbox_move_down)
        self.refresh_list()

        # Reorganization of the collection
        f_order = tk.Frame(self.left_panel, bg="#dfe6e9")
        f_order.pack(fill=tk.X, pady=2)
        tk.Button(f_order, text="▲", command=lambda: self.move_pattern(-1)).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(f_order, text="▼", command=lambda: self.move_pattern(1)).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Add/Rename/Copy/Delete pattern
        f_btns = tk.Frame(self.left_panel, bg="#dfe6e9", bd=0, highlightthickness=0)
        f_btns.pack(fill=tk.X, pady=5)
        #   - Use of columns with different weight to balance "+" and "-" button and "Rename" and "Copy" ones
        f_btns.grid_columnconfigure((0, 3), weight=1, uniform="group_p")
        f_btns.grid_columnconfigure((1, 2), weight=2, uniform="group_l")
        tk.Button(f_btns, text="➕", command=self.add_pattern, 
                  font=('Arial', 12, '')).grid(row=0, column=0, sticky="nsew", padx=(0, 1))
        self.txt_rename_patt=tk.StringVar(value=self.tr('rename_pattern'))
        tk.Button(f_btns, textvariable=self.txt_rename_patt, command=self.rename_pattern, 
                  font=('Arial', 8)).grid(row=0, column=1, sticky="nsew", padx=1)
        self.txt_copy_patt=tk.StringVar(value=self.tr('copy_pattern'))
        tk.Button(f_btns, textvariable=self.txt_copy_patt, command=self.duplicate_pattern, 
                  font=('Arial', 8)).grid(row=0, column=2, sticky="nsew", padx=1)
        tk.Button(f_btns, text="➖", command=self.delete_pattern, 
                  font=('Arial', 12, '')).grid(row=0, column=3, sticky="nsew", padx=(1, 0))

        # Collection mass change
        self.txt_apply_sel=tk.StringVar(value=self.tr('apply_selection'))
        tk.Button(self.left_panel, textvariable=self.txt_apply_sel, command=self.apply_settings_to_selection, bg="#fffa65", font=('Arial', 8, 'bold')).pack(fill=tk.X, pady=5)

        # Collection Import/Export
        self.txt_import_json=tk.StringVar(value=self.tr('import_json'))
        tk.Button(self.left_panel, textvariable=self.txt_import_json, command=self.import_collection, font=('Arial', 8)).pack(fill=tk.X, pady=2)
        self.txt_export_json=tk.StringVar(value=self.tr('export_json'))
        tk.Button(self.left_panel, textvariable=self.txt_export_json, command=self.export_collection, font=('Arial', 8)).pack(fill=tk.X, pady=2)
        
        # Batch SVG generation
        self.txt_batch_svg_export=tk.StringVar(value=self.tr('batch_svg_export'))
        tk.Button(self.left_panel, textvariable=self.txt_batch_svg_export, command=self.batch_export_svg, bg="#55efc4", font=('Arial', 10, 'bold')).pack(fill=tk.X, pady=5)

        # ---------------------------------
        # --       CENTRAL PANEL         --
        # --      Pattern Creation       --
        # --------------------------------- 

        # --- Create the panel
        self.cntrl = tk.Frame(self.root, padx=10, pady=5, bg="#f1f3f5", width=260)
        self.cntrl.pack(side=tk.LEFT, fill=tk.Y)
        self.cntrl.pack_propagate(False)

        # --- Language Selector
        # ---------------------------------
        f_lang = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_lang.pack(side=tk.TOP, anchor="ne", padx=0, pady=0)

        tk.Label(f_lang, text="Lang.", font=('Arial',8), bg="#f1f3f5", padx=2).pack(side=tk.LEFT)
        self.lang_var = tk.StringVar(value=self.lang.upper())
        self.om_lang = tk.OptionMenu(f_lang, self.lang_var, "FR", "EN", 
                                     command=self._on_language_change)
        self.om_lang.config(
            width=3,
            anchor="center",
            font=('Arial', 8), # Use mono-spaced font to preserve icon alignment
            bg="#f1f3f5",
            activebackground="#56b3f1",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#b2bec3",
            indicatoron=False # Disable menu arrow 
        )
        self.om_lang.pack(side=tk.RIGHT, pady=2)

        # --- Grid and mass operation
        # ---------------------------------
        self.txt_label_grid=tk.StringVar(value=self.tr('label_grid'))
        self._add_label_var(self.txt_label_grid)

        # -- Grid size and apply
        cfg_frame = tk.Frame(self.cntrl, bg="#f1f3f5")
        cfg_frame.pack(fill=tk.X, pady=5)
        tk.Label(cfg_frame, text="x=", bg="#f1f3f5", padx=2).pack(side=tk.LEFT)
        self.ent_cols = tk.Entry(cfg_frame, width=3)
        self.ent_cols.pack(side=tk.LEFT)
        tk.Label(cfg_frame, text="y=", bg="#f1f3f5", padx=2).pack(side=tk.LEFT)
        self.ent_rows = tk.Entry(cfg_frame, width=3)
        self.ent_rows.pack(side=tk.LEFT)
        self.txt_apply_grid=tk.StringVar(value=self.tr('apply_grid'))
        tk.Button(cfg_frame, textvariable=self.txt_apply_grid, command=self.update_grid_size, padx=5).pack(side=tk.RIGHT, padx=(5,0))
        
        # -- Grid type selection
        f_grid_type = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_grid_type.pack(fill=tk.X, pady=(0, 5))
        self.txt_grid_orth = tk.StringVar(value=self.tr('grid_orthogonal'))
        self.txt_grid_iso = tk.StringVar(value=self.tr('grid_isometric'))
        tk.Radiobutton(f_grid_type, textvariable=self.txt_grid_orth, variable=self.grid_type, 
                       value="orthogonal", command=self._ui_update_and_save, bg="#f1f3f5", 
                       font=('Arial', 9)).pack(side=tk.LEFT, padx=(0, 10))
        tk.Radiobutton(f_grid_type, textvariable=self.txt_grid_iso, variable=self.grid_type, 
                       value="isometric", command=self._ui_update_and_save, bg="#f1f3f5", 
                       font=('Arial', 9)).pack(side=tk.LEFT)
        
        # -- Grid filling
        self.txt_fill_all=tk.StringVar(value=self.tr('fill_all'))
        tk.Button(self.cntrl, textvariable=self.txt_fill_all, command=self.fill_all_shapes, bg="#dee2e6").pack(fill=tk.X, pady=(5,0))
        #   - Filling option section
        self.txt_fill_options=tk.StringVar(value=self.tr('fill_options'))
        tk.Label(self.cntrl, textvariable=self.txt_fill_options, bg="#f1f3f5", 
                 font=('Arial', 8, 'bold')).pack(anchor=tk.W, pady=(5, 0))
        
        # Fill style dropdowns - 2 rows x 3 columns layout
        
        # Container for fill style options
        f_fill_container = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_fill_container.pack(fill=tk.X, pady=(2, 5))
        
        # Row 1: Labels
        f_fill_labels = tk.Frame(f_fill_container, bg="#f1f3f5")
        f_fill_labels.pack(fill=tk.X)
        f_fill_labels.grid_columnconfigure(0, weight=1, uniform="fill_col")
        f_fill_labels.grid_columnconfigure(1, weight=1, uniform="fill_col")
        f_fill_labels.grid_columnconfigure(2, weight=1, uniform="fill_col")
        
        self.txt_fill_free_label = tk.StringVar(value=self.tr('fill_free'))
        tk.Label(f_fill_labels, textvariable=self.txt_fill_free_label, bg="#f1f3f5", font=('Arial', 8)).grid(row=0, column=0, padx=2)
        
        self.txt_fill_occupied_label = tk.StringVar(value=self.tr('fill_occupied'))
        tk.Label(f_fill_labels, textvariable=self.txt_fill_occupied_label, bg="#f1f3f5", font=('Arial', 8)).grid(row=0, column=1, padx=2)
        
        self.txt_fill_loop_label = tk.StringVar(value=self.tr('fill_loop'))
        tk.Label(f_fill_labels, textvariable=self.txt_fill_loop_label, bg="#f1f3f5", font=('Arial', 8)).grid(row=0, column=2, padx=2)
        
        # Row 2: Dropdowns
        f_fill_dropdowns = tk.Frame(f_fill_container, bg="#f1f3f5")
        f_fill_dropdowns.pack(fill=tk.X)
        f_fill_dropdowns.grid_columnconfigure(0, weight=1, uniform="fill_col")
        f_fill_dropdowns.grid_columnconfigure(1, weight=1, uniform="fill_col")
        f_fill_dropdowns.grid_columnconfigure(2, weight=1, uniform="fill_col")
        
        translated_fill_styles = [self.tr(f"fill_style_{style}") for style in self.fill_styles_available]
        self.fill_style_free.set(self.tr(f"fill_style_{self.current_fill_style_free}"))
        self.dd_fill_free = tk.OptionMenu(f_fill_dropdowns, self.fill_style_free, *translated_fill_styles, command=self._on_fill_style_free_menu_change)
        self.dd_fill_free.config(
            width=12,
            anchor="center",
            font=('Lucida Console', 8), # Use mono-spaced font to preserve icon alignment
            bg="white",
            activebackground="#e1e1e1",
            relief="groove",
            highlightthickness=0,
            indicatoron=False # Disable menu arrow 
        )
        menu_interne = self.dd_fill_free["menu"]
        menu_interne.config(
            font=('Lucida Console', 8),
            bg="white",
            activebackground="#f0f0f0",
            activeforeground="black",
            tearoff=0
        )
        self.dd_fill_free.grid(row=0, column=0, padx=2, sticky="ew")
        
        self.fill_style_occupied.set(self.tr(f"fill_style_{self.current_fill_style_occupied}"))
        self.dd_fill_occupied = tk.OptionMenu(f_fill_dropdowns, self.fill_style_occupied, *translated_fill_styles, command=self._on_fill_style_occupied_menu_change)
        self.dd_fill_occupied.config(
            width=12,
            anchor="center",
            font=('Lucida Console', 8), # Use mono-spaced font to preserve icon alignment
            bg="white",
            activebackground="#e1e1e1",
            relief="groove",
            highlightthickness=0,
            indicatoron=False # Disable menu arrow 
        )
        menu_interne = self.dd_fill_occupied["menu"]
        menu_interne.config(
            font=('Lucida Console', 8),
            bg="white",
            activebackground="#f0f0f0",
            activeforeground="black",
            tearoff=0
        )
        self.dd_fill_occupied.grid(row=0, column=1, padx=2, sticky="ew")
        
        self.fill_style_loop.set(self.tr(f"fill_style_{self.current_fill_style_loop}"))
        self.dd_fill_loop = tk.OptionMenu(f_fill_dropdowns, self.fill_style_loop, *translated_fill_styles, command=self._on_fill_style_loop_menu_change)
        self.dd_fill_loop.config(
            width=12,
            anchor="center",
            font=('Lucida Console', 8), # Use mono-spaced font to preserve icon alignment
            bg="white",
            activebackground="#e1e1e1",
            relief="groove",
            highlightthickness=0,
            indicatoron=False # Disable menu arrow 
        )
        menu_interne = self.dd_fill_loop["menu"]
        menu_interne.config(
            font=('Lucida Console', 8),
            bg="white",
            activebackground="#f0f0f0",
            activeforeground="black",
            tearoff=0
        )
        self.dd_fill_loop.grid(row=0, column=2, padx=2, sticky="ew")
           
        self.txt_erase_all=tk.StringVar(value=self.tr('erase_all'))
        tk.Button(self.cntrl, textvariable=self.txt_erase_all, command=self.clear_all, bg="#fab1a0").pack(fill=tk.X, pady=5)

        self._add_seperator()

        # --- Tool section
        # --------------------------------- 
        self.txt_label_tools=tk.StringVar(value=self.tr('label_tools'))
        self._add_label_var(self.txt_label_tools)

        # -- Shape selection : Radio button + Menu + Color picker
        f_shape = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_shape.pack(fill=tk.X, pady=2)

        #   - Radio button
        self.txt_rb_shape = tk.StringVar(value=self.tr("tool_shapes"))
        self.rb_shape = tk.Radiobutton(f_shape, textvariable=self.txt_rb_shape, font=('Arial', 9),
                                       variable=self.active_tool, 
                                       value="circle", 
                                       command=self._change_tool_and_save, 
                                       bg="#f1f3f5")
        self.rb_shape.pack(side=tk.LEFT)
        
        #   - Shape color picker -- Must be set prior the Menu to appear on the right most side
        self.btn_col_shapes = tk.Canvas(f_shape, width=18, height=18, bg=self.color_shapes, 
                                        highlightthickness=1, highlightbackground="#ced4da", cursor="hand2")
        self.btn_col_shapes.pack(side=tk.RIGHT, padx=2)
        self.btn_col_shapes.bind("<Button-1>", lambda e: self.pick_color_shapes())

        #   - Shape selection menu
        self.shape_display_var.set(self.tr(f"shape_{self.current_shape_id}"))
        #     - Labels are translated on fly
        translated_labels = [self.tr(f"shape_{sid}") for sid in self.shapes_available]
        self.om_shape = tk.OptionMenu(f_shape, self.shape_display_var, *translated_labels, 
                                      command=self._on_shape_menu_change)
        self.om_shape.pack(side=tk.RIGHT)
        self.om_shape.config(
            width=12,
            anchor="center",
            font=('Lucida Console', 9), # Use mono-spaced font to preserve icon alignment
            bg="white",
            activebackground="#e1e1e1",
            relief="groove",
            highlightthickness=0,
            indicatoron=False # Disable menu arrow 
        )
        menu_interne = self.om_shape["menu"]
        menu_interne.config(
            font=('Lucida Console', 9),
            bg="white",
            activebackground="#f0f0f0",
            activeforeground="black",
            tearoff=0
        )

        # -- Drawing tool : Radio button + Color picker
        f_line = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_line.pack(fill=tk.X, pady=2)

        #   - Radio button
        self.txt_rb_drawing = tk.StringVar(value=self.tr("tool_drawing"))
        tk.Radiobutton(f_line, textvariable=self.txt_rb_drawing, variable=self.active_tool, value="line", 
                       command=self._change_tool_and_save, bg="#f1f3f5").pack(side=tk.LEFT)
        
        #   - Drawing color picker
        self.btn_col_lines = tk.Canvas(f_line, width=18, height=18, bg=self.color_lines, 
                                       highlightthickness=1, highlightbackground="#ced4da", cursor="hand2")
        self.btn_col_lines.pack(side=tk.RIGHT, padx=2)
        self.btn_col_lines.bind("<Button-1>", lambda e: self.pick_color_lines())

        self._add_seperator()

        # --- Parameter section
        # --------------------------------- 
        self.txt_label_param=tk.StringVar(value=self.tr('label_param'))
        self._add_label_var(self.txt_label_param)

        # -- Shape Type and Negative mode
        f_toggles = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_toggles.pack(fill=tk.X, pady=5)

        #   - Use grid to balance the 2 buttons
        f_toggles.grid_columnconfigure(0, weight=1, uniform="group1")
        f_toggles.grid_columnconfigure(1, weight=1, uniform="group1")

        #   - Left : Shape Type toggle button
        cell_left = tk.Frame(f_toggles, bg="#f1f3f5")
        cell_left.grid(row=0, column=0, sticky="ew", padx=2)
        #     - Use an extra frame to create a thick border emulating the "outlined"  
        self.border_outline = tk.Frame(cell_left, bg="black", padx=3, pady=3, highlightthickness=2, highlightcolor="#000000")
        self.border_outline.pack(fill=tk.X)

        self.btn_outline = tk.Button(self.border_outline, text=self.tr('btn_outline_on'), 
                                     font=('Arial', 9, 'bold'),
                                     bg="white", fg="black",
                                     relief="groove", bd=0,
                                     command=self.toggle_outline)
        self.btn_outline.pack(fill=tk.X)

        #   - Right : Negative toggle button
        cell_right = tk.Frame(f_toggles, bg="#f1f3f5")
        cell_right.grid(row=0, column=1, sticky="ew", padx=2)
        #     - Use same extra frame as the shape type button
        self.border_negative = tk.Frame(cell_right, bg="#ced4da", padx=3, pady=3, highlightthickness=2, highlightcolor="#000000")
        self.border_negative.pack(fill=tk.X)

        self.btn_negative = tk.Button(self.border_negative, text=self.tr('btn_neg_off'), 
                                      font=('Arial', 9, 'bold'),
                                      bg="white", fg="black",
                                      relief="groove", bd=0,
                                      command=self.toggle_negative)
        self.btn_negative.pack(fill=tk.X)

        # -- Scales for item sizing
        self.txt_sc_shape_size=tk.StringVar(value=self.tr('shape_size'))
        self._add_horizontal_scale_var(self.cntrl, self.txt_sc_shape_size, self.shape_size_ratio, 0.1, 2.0, 0.1)
        self.txt_sc_outline_width=tk.StringVar(value=self.tr('outline_width'))
        self._add_horizontal_scale_var(self.cntrl, self.txt_sc_outline_width, self.shape_stroke_pct, 0, 100)
        self.txt_sc_lines_width=tk.StringVar(value=self.tr('lines_width'))
        self._add_horizontal_scale_var(self.cntrl, self.txt_sc_lines_width, self.line_stroke_width, 0, 100)
        self.txt_sc_index_ratio=tk.StringVar(value=self.tr('index_ratio'))
        self._add_horizontal_scale_var(self.cntrl, self.txt_sc_index_ratio, self.index_ratio, 0.1, 1.0, 0.05)

        self._add_seperator()
        
        # --- Options section
        # --------------------------------- 
        self.txt_label_options=tk.StringVar(value=self.tr('label_options'))
        self._add_label_var(self.txt_label_options)

        # -- Main options
        self.txt_show_grid=tk.StringVar(value=self.tr('show_grid'))
        tk.Checkbutton(self.cntrl, textvariable=self.txt_show_grid, variable=self.show_grid, command=self._ui_update_and_save, bg="#f1f3f5").pack(anchor=tk.W)
        self.txt_show_shapes=tk.StringVar(value=self.tr('show_shapes'))
        tk.Checkbutton(self.cntrl, textvariable=self.txt_show_shapes, variable=self.show_shapes, command=self._ui_update_and_save, bg="#f1f3f5").pack(anchor=tk.W)
        self.txt_show_lines=tk.StringVar(value=self.tr('show_lines'))
        tk.Checkbutton(self.cntrl, textvariable=self.txt_show_lines, variable=self.show_lines, command=self._ui_update_and_save, bg="#f1f3f5").pack(anchor=tk.W)
        self.txt_crop_grid=tk.StringVar(value=self.tr('crop_grid'))
        tk.Checkbutton(self.cntrl, textvariable=self.txt_crop_grid, variable=self.crop_to_grid, command=self._ui_update_and_save, bg="#f1f3f5", fg="#0984e3").pack(anchor=tk.W)
        
        # -- Index creation : Check button + Option Menu + Color picker -- Similar to Shape tool
        f_index = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_index.pack(fill=tk.X, pady=2)
        
        #     - Check button 
        self.txt_add_index=tk.StringVar(value=self.tr('add_index'))
        tk.Checkbutton(f_index, textvariable=self.txt_add_index, variable=self.show_index, 
                       command=self._ui_update_and_save, bg="#f1f3f5", font=('Arial', 9)).pack(side=tk.LEFT)

        #     - Index color picker - Must be set prior the menu to appear on the right most side
        self.btn_col_index = tk.Canvas(f_index, width=18, height=18, bg=self.color_index, 
                                        highlightthickness=1, highlightbackground="#ced4da", cursor="hand2")
        self.btn_col_index.pack(side=tk.RIGHT, padx=2)
        self.btn_col_index.bind("<Button-1>", lambda e: self.pick_color_index())

        #     - Option menu
        self.index_pos_var.set(self.tr(f"pos_{self.current_index_pos_id}"))
        translated_pos_labels = [self.tr(f"pos_{pid}") for pid in self.index_pos_available]       
        self.om_pos = tk.OptionMenu(f_index, self.index_pos_var, *translated_pos_labels, 
                                    command=self._on_index_pos_menu_change)
        self.om_pos.pack(side=tk.RIGHT)
        self.om_pos.config(
            width=12,
            anchor="center",
            font=('Lucida Console', 9),
            bg="white",
            activebackground="#e1e1e1", 
            relief="groove",
            highlightthickness=0,
            indicatoron=False
        )
        menu_interne = self.om_pos["menu"]
        menu_interne.config(
            font=('Lucida Console', 9),
            bg="white",
            activebackground="#f0f0f0",
            activeforeground="black",
            borderwidth=1,
            tearoff=0
        )

        # --- Transform section
        # ---------------------------------
        self._add_seperator()
        
        self.txt_label_transform=tk.StringVar(value=self.tr('label_transform'))
        self._add_label_var(self.txt_label_transform)

        # -- Transformation buttons
        f_transform = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_transform.pack(fill=tk.X, pady=5)
        f_transform.grid_columnconfigure((0, 1), weight=1, uniform="group_t")
        
        self.txt_scale = tk.StringVar(value=self.tr('transform_scale'))
        tk.Button(f_transform, textvariable=self.txt_scale, command=self.transform_scale, 
                  font=('Arial', 8)).grid(row=0, column=0, sticky="ew", padx=2)
        
        self.txt_shift = tk.StringVar(value=self.tr('transform_shift'))
        tk.Button(f_transform, textvariable=self.txt_shift, command=self.transform_shift, 
                  font=('Arial', 8)).grid(row=0, column=1, sticky="ew", padx=2)
        
        f_transform2 = tk.Frame(self.cntrl, bg="#f1f3f5")
        f_transform2.pack(fill=tk.X, pady=2)
        f_transform2.grid_columnconfigure((0, 1), weight=1, uniform="group_t")
        
        self.txt_copy_shift = tk.StringVar(value=self.tr('transform_copy_shift'))
        tk.Button(f_transform2, textvariable=self.txt_copy_shift, command=self.transform_copy_shift, 
                  font=('Arial', 8)).grid(row=0, column=0, sticky="ew", padx=2)
        
        self.txt_symmetry = tk.StringVar(value=self.tr('transform_symmetry'))
        tk.Button(f_transform2, textvariable=self.txt_symmetry, command=self.transform_symmetry, 
                  font=('Arial', 8)).grid(row=0, column=1, sticky="ew", padx=2)

        # --- Generate SVG button
        # ---------------------------------
        self.txt_gen_svg=tk.StringVar(value=self.tr('gen_svg'))
        tk.Button(self.cntrl, textvariable=self.txt_gen_svg, command=self.export_svg, bg="#2ecc71", fg="white", font=('Arial', 10, 'bold')).pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # --- Canvas creation
        # ---------------------------------
        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=700, highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.canvas.bind("<Button-1>", self._on_canvas_click)
    #--------------------------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------------------------------------
    #  UI Methods
    #--------------------------------------------------------------------------------------------------------
    
    def pick_color_shapes(self):
        c = colorchooser.askcolor(color=self.color_shapes)[1]
        if c: self.color_shapes = c; self.btn_col_shapes.config(bg=c); self._sync_btn_outline(); self._ui_update_and_save()
    
    def pick_color_lines(self):
        c = colorchooser.askcolor(color=self.color_lines)[1]
        if c: self.color_lines = c; self.btn_col_lines.config(bg=c); self._ui_update_and_save()
    
    def pick_color_index(self):
        c = colorchooser.askcolor(color=self.color_index)[1]
        if c: self.color_index = c; self.btn_col_index.config(bg=c); self._ui_update_and_save()
    
    def _get_contrast_color(self, hex_c):
        r, g, b = int(hex_c[1:3], 16), int(hex_c[3:5], 16), int(hex_c[5:7], 16)
        return "black" if (0.299*r + 0.587*g + 0.114*b)/255 > 0.5 else "white"

    def _add_label(self, txt): tk.Label(self.cntrl, text=txt, font=('Arial', 9, 'bold'), bg="#f1f3f5").pack(anchor=tk.W)
    def _add_label_var(self, txtvar): tk.Label(self.cntrl, textvariable=txtvar, font=('Arial', 9, 'bold'), bg="#f1f3f5").pack(anchor=tk.W)
       
    def _add_seperator(self): tk.Frame(self.cntrl, height=1, bg="#adb5bd").pack(fill=tk.X, pady=10)
    
    def _add_horizontal_scale(self, parent, text, variable, from_, to_, resolution=1):
        frame = tk.Frame(parent, bg="#f1f3f5") # Line container
        frame.pack(fill=tk.X, pady=2)
        
        # Label: Name
        lbl = tk.Label(frame, text=text, font=('Arial', 9), bg="#f1f3f5", # Text aligned on the left with the anchor
                       width=12, anchor=tk.W)
        lbl.pack(side=tk.LEFT, padx=(1, 0)) # Label is centered verticaly with the pax

        # Scale
        scale = tk.Scale(frame, from_=from_, to=to_, resolution=resolution, 
                         orient=tk.HORIZONTAL, variable=variable, 
                         command=self._ui_update_and_save, 
                         bg="#f1f3f5", bd=0, highlightthickness=0, 
                         showvalue=False) # Remove show value to streamline the dispay and compact it 
        scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Label: Scale value using textvariable for auto update
        val_lbl = tk.Label(frame, textvariable=variable, font=('Arial', 9, 'bold'), 
                           bg="#f1f3f5", width=5, anchor=tk.E)
        val_lbl.pack(side=tk.LEFT, padx=(0, 1))

        return scale

    def _add_horizontal_scale_var(self, parent, textvar, variable, from_, to_, resolution=1):
        frame = tk.Frame(parent, bg="#f1f3f5") # Line container
        frame.pack(fill=tk.X, pady=2)
        
        # Label: Name
        lbl = tk.Label(frame, textvariable=textvar, font=('Arial', 9), bg="#f1f3f5", # Text aligned on the left with the anchor
                       width=12, anchor=tk.W)
        lbl.pack(side=tk.LEFT, padx=(1, 0)) # Label is centered verticaly with the pax

        # Scale
        scale = tk.Scale(frame, from_=from_, to=to_, resolution=resolution, 
                         orient=tk.HORIZONTAL, variable=variable, 
                         command=self._ui_update_and_save, 
                         bg="#f1f3f5", bd=0, highlightthickness=0, 
                         showvalue=False) # Remove show value to streamline the dispay and compact it 
        scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=0)

        # Label: Scale value using textvariable for auto update
        val_lbl = tk.Label(frame, textvariable=variable, font=('Arial', 9, 'bold'), 
                           bg="#f1f3f5", width=4, anchor=tk.E)
        val_lbl.pack(side=tk.LEFT, padx=(0, 1))

        return scale

    def _ask_custom_string(self, title, prompt, initial=""):
        self.root.update_idletasks()
        result = {"value": None}
        
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("340x130")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centered from parent window
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 140
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 65
        dialog.geometry(f"+{x}+{y}")

        tk.Label(dialog, text=prompt, anchor="w", justify=tk.LEFT).pack(fill=tk.X, padx=20, pady=(15, 5))
        
        entry = tk.Entry(dialog)
        entry.pack(fill=tk.X, padx=20, pady=5)
        entry.insert(0, initial)
        entry.select_range(0, tk.END)
        entry.focus_set()

        def validate(event=None):
            val = entry.get().strip()
            if val:
                result["value"] = val
                dialog.destroy()

        # Aligned button as for simpledialog
        f_btns = tk.Frame(dialog)
        f_btns.pack(fill=tk.X, padx=20, pady=15)
        tk.Button(f_btns, text=self.tr('btn_ok'), width=9, command=validate, default=tk.ACTIVE).pack(side=tk.RIGHT, padx=(5, 0))
        tk.Button(f_btns, text=self.tr('btn_cancel'), width=9, command=dialog.destroy).pack(side=tk.RIGHT)

        dialog.bind("<Return>", validate)
        dialog.bind("<Escape>", lambda e: dialog.destroy())
        
        self.root.wait_window(dialog)
        return result["value"]

    def _ask_custom_confirm(self, title_key, prompt_key):
        self.root.update_idletasks()
        result = {"value": False}
        
        dialog = tk.Toplevel(self.root)
        dialog.title(self.tr(title_key))
        dialog.geometry("340x130")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centered from parent window
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 140
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 55
        dialog.geometry(f"+{x}+{y}")

        # Message
        tk.Label(dialog, text=self.tr(prompt_key), anchor="w", justify=tk.LEFT).pack(fill=tk.X, padx=20, pady=(20, 10))
        
        def confirm():
            result["value"] = True
            dialog.destroy()

        # Aligned button as for simpledialog
        f_btns = tk.Frame(dialog)
        f_btns.pack(fill=tk.X, padx=20, pady=10)
        btn_yes = tk.Button(f_btns, text=self.tr("btn_yes"), width=9, 
                            command=confirm, default=tk.ACTIVE)
        btn_yes.pack(side=tk.RIGHT, padx=(5, 0))
        btn_no = tk.Button(f_btns, text=self.tr("btn_no"), width=9, 
                           command=dialog.destroy)
        btn_no.pack(side=tk.RIGHT)

        # Keyboard binding
        dialog.bind("<Return>", lambda e: confirm())
        dialog.bind("<Escape>", lambda e: dialog.destroy())
        
        btn_yes.focus_set() # Le focus est sur Oui par défaut
        
        self.root.wait_window(dialog)
        return result["value"]
    
    def toggle_outline(self):
        self.use_outlined_shape.set(not self.use_outlined_shape.get())
        self._sync_btn_outline()
        self._ui_update_and_save()

    def toggle_negative(self):
        self.negative_mode.set(not self.negative_mode.get())
        self._sync_btn_neg()
        self._sync_btn_outline()
        self._ui_update_and_save()

    def _sync_btn_neg(self):
        if not self.negative_mode.get():
            self.btn_negative.config(bg="white", fg="black", text=self.tr('btn_neg_off'))
        else:
            self.btn_negative.config(bg="black", fg="white", text=self.tr('btn_neg_on'))

    def _sync_btn_outline(self):
        if not self.negative_mode.get():
            self.border_outline.config(bg=self.color_shapes, padx=3, pady=3)
            if not self.use_outlined_shape.get():
                self.btn_outline.config(text=self.tr('btn_outline_off'),
                bg=self.color_shapes, fg=self._get_contrast_color(self.color_shapes))
            else:
                self.btn_outline.config(text=self.tr('btn_outline_on'),
                bg="White", fg=self.color_shapes)
        else:
            self.border_outline.config(bg="white", padx=3, pady=3)
            if self.use_outlined_shape.get():
                self.btn_outline.config(text=self.tr('btn_outline_on'),
                bg=self.color_shapes, fg=self._get_contrast_color(self.color_shapes))
            else:
                self.btn_outline.config(text=self.tr('btn_outline_off'),
                bg="White", fg=self.color_shapes)

    def refresh_ui_language(self, prev_default_patt_name=""):

        self.title_var.set(self.tr("main_title").format(VERSION,self.current_pattern_name))

        self.txt_rename_coll.set(self.tr('rename_collection'))
        self.txt_rename_patt.set(self.tr('rename_pattern'))
        self.txt_copy_patt.set(self.tr('copy_pattern'))
        self.txt_apply_sel.set(self.tr('apply_selection'))
        self.txt_import_json.set(self.tr('import_json'))
        self.txt_export_json.set(self.tr('export_json'))
        self.txt_batch_svg_export.set(self.tr('batch_svg_export'))

        self.txt_label_grid.set(self.tr('label_grid'))
        self.txt_apply_grid.set(self.tr('apply_grid'))
        self.txt_grid_orth.set(self.tr('grid_orthogonal'))
        self.txt_grid_iso.set(self.tr('grid_isometric'))
        self.txt_fill_all.set(self.tr('fill_all'))
        self.txt_fill_options.set(self.tr('fill_options'))
        self.txt_fill_free_label.set(self.tr('fill_free'))
        self.txt_fill_occupied_label.set(self.tr('fill_occupied'))
        self.txt_fill_loop_label.set(self.tr('fill_loop'))
        # Update Fill Style Option Menus
        self.fill_style_free.set(self.tr(f"fill_style_{self.current_fill_style_free}"))
        menu = self.dd_fill_free["menu"]
        menu.delete(0, "end")
        for style in self.fill_styles_available:
            label = self.tr(f"fill_style_{style}")
            menu.add_command(label=label, 
                             command=lambda l=label: self.om_fill_style_free_set(l))

        self.fill_style_occupied.set(self.tr(f"fill_style_{self.current_fill_style_occupied}"))
        menu = self.dd_fill_occupied["menu"]
        menu.delete(0, "end")
        for style in self.fill_styles_available:
            label = self.tr(f"fill_style_{style}")
            menu.add_command(label=label, 
                             command=lambda l=label: self.om_fill_style_occupied_set(l))

        self.fill_style_loop.set(self.tr(f"fill_style_{self.current_fill_style_loop}"))
        menu = self.dd_fill_loop["menu"]
        menu.delete(0, "end")
        for style in self.fill_styles_available:
            label = self.tr(f"fill_style_{style}")
            menu.add_command(label=label, 
                             command=lambda l=label: self.om_fill_style_loop_set(l))

        self.txt_erase_all.set(self.tr('erase_all'))

        self.txt_rb_shape.set(self.tr("tool_shapes"))       
        # Update Tool Option Menu
        self.shape_display_var.set(self.tr(f"shape_{self.current_shape_id}"))
        menu = self.om_shape["menu"]
        menu.delete(0, "end")
        for sid in self.shapes_available:
            label = self.tr(f"shape_{sid}")
            menu.add_command(label=label, 
                             command=lambda l=label: self.om_shape_set(l))
        
        self.txt_rb_drawing.set(self.tr("tool_drawing"))

        self.txt_label_param.set(self.tr('label_param'))
        self._sync_btn_neg()
        self._sync_btn_outline()

        self.txt_sc_shape_size.set(self.tr('shape_size'))
        self.txt_sc_outline_width.set(self.tr('outline_width'))
        self.txt_sc_lines_width.set(self.tr('lines_width'))
        self.txt_sc_index_ratio.set(self.tr('index_ratio'))

        self.txt_label_options.set(self.tr('label_options'))

        self.txt_show_grid.set(self.tr('show_grid'))
        self.txt_show_lines.set(self.tr('show_lines'))
        self.txt_show_shapes.set(self.tr('show_shapes'))   
        self.txt_crop_grid.set(self.tr('crop_grid'))
        self.txt_add_index.set(self.tr('add_index'))
        # Update Index Position Option Menu
        self.index_pos_var.set(self.tr(f"pos_{self.current_index_pos_id}"))
        menu = self.om_pos["menu"]
        menu.delete(0, "end")
        for sid in self.index_pos_available:
            label = self.tr(f"pos_{sid}")
            menu.add_command(label=label, 
                             command=lambda l=label: self.om_index_set(l))   
        
        self.txt_label_transform.set(self.tr('label_transform'))
        self.txt_scale.set(self.tr('transform_scale'))
        self.txt_shift.set(self.tr('transform_shift'))
        self.txt_copy_shift.set(self.tr('transform_copy_shift'))
        self.txt_symmetry.set(self.tr('transform_symmetry'))
        
        self.txt_gen_svg.set(self.tr('gen_svg'))

        # If there is only the default pattern in the collection, rename it.
        if len(self.order) == 1 and self.order[0] == prev_default_patt_name+" 1":
            old=self.order[0]
            new=self.tr('default_pattern_name')+" 1"
            if new not in self.collection:
                # Change the key of the collection dictionary
                self.collection[new] = self.collection.pop(old)
                # Update the list
                self.order[self.order.index(old)] = new
                self.current_pattern_name = new
                self.refresh_list()
                # Reload the new name to check the reindexing
                self.load_pattern_from_collection(new)

    def om_shape_set(self, label):
        self.shape_display_var.set(label)
        self._on_shape_menu_change(label)

    def om_index_set(self, label):
        self.index_pos_var.set(label)
        self._on_index_pos_menu_change(label)

    def om_fill_style_free_set(self, label):
        self.fill_style_free.set(label)
        self._on_fill_style_free_menu_change(label)

    def om_fill_style_occupied_set(self, label):
        self.fill_style_occupied.set(label)
        self._on_fill_style_occupied_menu_change(label)

    def om_fill_style_loop_set(self, label):
        self.fill_style_loop.set(label)
        self._on_fill_style_loop_menu_change(label)

    def _on_language_change(self, selected_lang):
        # Save previous language default pattern name before switching
        prev_default_pattern_name=self.tr('default_pattern_name')

        # Use lowercase for dictionnary entry
        new_lang = selected_lang.lower()
        
        if new_lang != self.lang:
            self.lang = new_lang
            # Update the ui
            self.refresh_ui_language(prev_default_pattern_name)

    #--------------------------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------------------------------------
    #  Utils
    #--------------------------------------------------------------------------------------------------------
    def tr(self, key):
        # Get text from selected language
        return LANGUAGES[self.lang].get(key, key) # Return key value if text not available
    
    def _clean_filename(self, name):    
        # Replace everything NOT (a-z, A-Z, 0-9) with "_"
        clean = re.sub(r'[^a-zA-Z0-9]', '_', name)
        # Remove double '_'
        return re.sub(r'_+', '_', clean).strip('_')

    def _get_blank_state(self):
        return {
            "cols": self.cols, "rows": self.rows, "shape_ratio": self.shape_size_ratio.get(), "stroke_pct": self.shape_stroke_pct.get(), "use_outline": True,
            "line_sw": self.line_stroke_width.get(), "c_shapes": self.color_shapes, "c_lines": self.color_lines,
            "neg": self.negative_mode.get(), "tool": self.current_shape_id, "shapes": {}, "lines": set(), "blocked_nodes": set(), "grid_type": self.grid_type.get(),
            "fill_style_free": self.current_fill_style_free, "fill_style_occupied": self.current_fill_style_occupied, "fill_style_loop": self.current_fill_style_loop
        }
    
    def _ui_update_and_save(self, _=None):
        self._sync_shapes_style()
        self.save_to_collection()
        self.draw_canvas()  
    
    def _change_tool_and_save(self):
        new_tool = self.active_tool.get()
        # If new shape is selected, update the tool of the pattern
        if new_tool in ['circle', 'square']:
            self.collection[self.current_pattern_name]['tool'] = new_tool
        # If drawing tool is selected, show the lines
        if new_tool == "line": 
            self.show_lines.set(True)
        else: # If shape tool is selected, show the shapes
            self.show_shapes.set(True)
        # Save and refresh display
        self._ui_update_and_save()
            
    def _sync_shapes_style(self):
        if not self.use_outlined_shape.get():
            for key in self.pattern_shapes:
                self.pattern_shapes[key] = "full"

    def _sync_shape_selector(self, tool_value):
        # Update shape selector
        if tool_value in self.shapes_available:
            self.current_shape_id = tool_value
            self.active_tool.set(tool_value)
            self.rb_shape.config(value=tool_value)
            self.om_shape_set(self.tr(f"shape_{tool_value}"))

    def _sync_fill_style(self):
        self.om_fill_style_free_set(self.tr(f"fill_style_{self.current_fill_style_free}"))
        self.om_fill_style_occupied_set(self.tr(f"fill_style_{self.current_fill_style_occupied}"))
        self.om_fill_style_loop_set(self.tr(f"fill_style_{self.current_fill_style_loop}"))

    def _on_shape_menu_change(self, display_value):
        # Convert displayed value to usable one
        # by finding the proper name matching
        tech_value = None
        for sid in self.shapes_available:
            if self.tr(f"shape_{sid}") == display_value:
                tech_value = sid
                break
        
        if tech_value:
            self.current_shape_id = tech_value
            # Update radio button
            self.rb_shape.config(value=self.current_shape_id)
            # Activate the Tool
            self.active_tool.set(self.current_shape_id)
            # Save 
            self._change_tool_and_save()

    def _on_fill_style_free_menu_change(self, display_value):
        # Retrive technical value
        for pid in self.fill_styles_available:
            if self.tr(f"fill_style_{pid}") == display_value:
                self.current_fill_style_free = pid
                break
        self._ui_update_and_save()

    def _on_fill_style_occupied_menu_change(self, display_value):
        # Retrive technical value
        for pid in self.fill_styles_available:
            if self.tr(f"fill_style_{pid}") == display_value:
                self.current_fill_style_occupied = pid
                break
        self._ui_update_and_save()

    def _on_fill_style_loop_menu_change(self, display_value):
        # Retrive technical value
        for pid in self.fill_styles_available:
            if self.tr(f"fill_style_{pid}") == display_value:
                self.current_fill_style_loop = pid
                break
        self._ui_update_and_save()

    def _on_index_pos_menu_change(self, display_value):
        # Enable Index display
        self.show_index.set(True)
        # Retrive technical value
        for pid in self.index_pos_available:
            if self.tr(f"pos_{pid}") == display_value:
                self.current_index_pos_id = pid
                break
        self._ui_update_and_save()

    def _get_index_triangle_points(self, ox, oy, dy, size):

        ty = oy
        tri_size = size * self.index_ratio.get()
        h = (math.sqrt(3)/2) * tri_size
        
        pos = self.current_index_pos_id
        if pos == "left": # Pointing to the border of the grid
            return [(ox - h, ty - tri_size/2), (ox - h, ty + tri_size/2), (ox, ty)]
        elif pos == "centred": # Optic alignement for a centred position (using Barycenter 1/3 - 2/3 and 1/2 size)
            return [(ox - h/3, ty - tri_size/2), (ox - h/3, ty + tri_size/2), (ox + 2*h/3, ty)]
        elif pos == "edge":  # Vertical side is at the edge of the shape (ox - size/2)
            start_x = ox - size/2
            return [(start_x, ty - tri_size/2), (start_x, ty + tri_size/2), (start_x + h, ty)]
        else: # "right" # Vertical side is at the edge of the grid
            return [(ox, ty - tri_size/2), (ox, ty + tri_size/2), (ox + h, ty)]
    #--------------------------------------------------------------------------------------------------------
         
    #--------------------------------------------------------------------------------------------------------
    #  Collection Management Methods
    #--------------------------------------------------------------------------------------------------------

    # Rename the collection
    #----------------------------
    def rename_collection(self):
        new = self._ask_custom_string(self.tr('rename_coll_title'), self.tr('rename_coll_txt'), self.collection_name)
        if new:
            self.collection_name = new
            self.lbl_coll_name.config(text=new)

    def on_close(self):
        if messagebox.askokcancel(self.tr('close_confirm_title'), self.tr('close_confirm_txt')):
            self.root.destroy()

    # Save/Load/Apply to/from collection
    #----------------------------
    def save_to_collection(self):
        if not self.current_pattern_name: return  

        self.collection[self.current_pattern_name] = {
            "cols": self.cols, "rows": self.rows, 
            "shape_ratio": self.shape_size_ratio.get(),
            "stroke_pct": self.shape_stroke_pct.get(), 
            "line_sw": self.line_stroke_width.get(),
            "c_shapes": self.color_shapes, 
            "c_lines": self.color_lines,
            "neg": self.negative_mode.get(), 
            "tool": self.current_shape_id,
            "shapes": self.pattern_shapes.copy(), 
            "lines": self.pattern_lines.copy(),
            "blocked_nodes":self.blocked_nodes.copy(),
            "grid_type": self.grid_type.get(),
            "fill_style_free": self.current_fill_style_free,
            "fill_style_occupied": self.current_fill_style_occupied,
            "fill_style_loop": self.current_fill_style_loop
        }

    def load_pattern_from_collection(self, name):
        self.current_pattern_name = name
        d = self.collection[name]
        self.cols, self.rows = d["cols"], d["rows"]
        self.ent_cols.delete(0, tk.END); self.ent_cols.insert(0, str(self.cols))
        self.ent_rows.delete(0, tk.END); self.ent_rows.insert(0, str(self.rows))
        self.shape_size_ratio.set(d["shape_ratio"])
        self.shape_stroke_pct.set(d["stroke_pct"])
        self.line_stroke_width.set(d["line_sw"])
        self.color_shapes, self.color_lines = d["c_shapes"], d["c_lines"]
        self.negative_mode.set(d["neg"])
        # Sync of the tool
        # if the current tool is not the drawing one, 
        # toogle the selected tool to match loaded shape
        stored_tool = d.get("tool", "circle")
        if self.active_tool.get() != "line":
            self.active_tool.set(stored_tool)
            self._sync_shape_selector(stored_tool)
        self.pattern_shapes, self.pattern_lines = d["shapes"].copy(), d["lines"].copy()
        self.blocked_nodes = d.get("blocked_nodes", set()).copy()
        self.grid_type.set(d.get("grid_type", "orthogonal"))
        # Load fill styles with defaults for backward compatibility
        self.current_fill_style_free = d.get("fill_style_free", "plain")
        self.current_fill_style_occupied = d.get("fill_style_occupied", "void")
        self.current_fill_style_loop = d.get("fill_style_loop", "outline")
        self.btn_col_shapes.config(bg=self.color_shapes)
        self.btn_col_lines.config(bg=self.color_lines)
        self._sync_btn_neg()
        self._sync_btn_outline()
        self._sync_fill_style()
        self.draw_canvas()
        self.title_var.set(self.tr("main_title").format(VERSION,self.current_pattern_name))

    def apply_settings_to_selection(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices: return
        if not self._ask_custom_confirm(self.tr('apply_to_sel_confirm_title'), self.tr('apply_to_sel_confirm_txt')): return

        # Create a set of settings to appy 
        # - Use current pattern shape used instead of the active tool
        master_tool = self.collection[self.current_pattern_name].get('tool', 'circle')
        use_outline = self.use_outlined_shape.get()
        master = {
            "cols": self.cols, "rows": self.rows, "shape_ratio": self.shape_size_ratio.get(),
            "stroke_pct": self.shape_stroke_pct.get(), "line_sw": self.line_stroke_width.get(),
            "c_shapes": self.color_shapes, "c_lines": self.color_lines,
            "neg": self.negative_mode.get(), "tool": master_tool,
            "fill_style_free": self.current_fill_style_free, 
            "fill_style_occupied": self.current_fill_style_occupied,
            "fill_style_loop": self.current_fill_style_loop,
            "use_outline": use_outline, "grid_type": self.grid_type.get()
        }

        for idx in selected_indices:
            name = self.listbox.get(idx)
            self.collection[name].update(master)
            # Transform every outlined shape to full one in case the outline option is not set
            if not use_outline:
                for key in self.collection[name]["shapes"]:
                    self.collection[name]["shapes"][key] = "full"

        messagebox.showinfo(self.tr('apply_to_sel_done_title'),self.tr('apply_to_sel_done_txt'))
        self.draw_canvas()

    # List management
    #----------------------------
    def on_list_select(self, e):
        sel = self.listbox.curselection()
        if sel and len(sel) == 1:
            self.save_to_collection()             
            new_name = self.listbox.get(sel[0])
            if new_name != self.current_pattern_name:
                self.load_pattern_from_collection(new_name)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for name in self.order: 
            self.listbox.insert(tk.END, name)

        # Check current pattern name exists in the list and focus on it
        if self.current_pattern_name and self.current_pattern_name in self.order:
            idx = self.order.index(self.current_pattern_name)
            # Force selection of the current item
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(idx)
            self.listbox.activate(idx)
            self.listbox.see(idx)

    def _on_listbox_delete_key(self, event=None):
        self.delete_pattern()
        return "break"

    def _on_listbox_move_up(self, event=None):
        self.move_pattern(-1)
        return "break"

    def _on_listbox_move_down(self, event=None):
        self.move_pattern(1)
        return "break"

    def _bind_shortcuts(self):
        self.root.bind_all('<Control-a>', self._on_ctrl_add)
        self.root.bind_all('<Control-A>', self._on_ctrl_add)
        self.root.bind_all('<Control-d>', self._on_ctrl_duplicate)
        self.root.bind_all('<Control-D>', self._on_ctrl_duplicate)
        self.root.bind_all('<Control-r>', self._on_ctrl_rename)
        self.root.bind_all('<Control-R>', self._on_ctrl_rename)
        self.root.bind_all('<Control-Delete>', self._on_ctrl_delete)

    def _on_ctrl_add(self, event=None):
        self.add_pattern()
        return "break"

    def _on_ctrl_duplicate(self, event=None):
        self.duplicate_pattern()
        return "break"

    def _on_ctrl_rename(self, event=None):
        self.rename_pattern()
        return "break"

    def _on_ctrl_delete(self, event=None):
        self.delete_pattern()
        return "break"

    def _on_listbox_rename_key(self, event=None):
        sel = self.listbox.curselection()
        if not sel or len(sel) != 1:
            return "break"

        idx = sel[0]
        old_name = self.order[idx]
        bbox = self.listbox.bbox(idx)
        if not bbox:
            return "break"

        x, y, w, h = bbox
        width = self.listbox.winfo_width() - 4
        entry = tk.Entry(self.listbox)
        entry.insert(0, old_name)
        entry.select_range(0, tk.END)
        entry.focus_set()
        entry.place(x=2, y=y, width=width, height=h)

        def commit(event=None):
            new_name = entry.get().strip()
            if new_name and new_name != old_name:
                if new_name in self.collection:
                    messagebox.showerror(self.tr('error'), self.tr('err_exists'))
                    return "break"
                self._apply_inline_pattern_rename(old_name, new_name)
            entry.destroy()
            return "break"

        def cancel(event=None):
            entry.destroy()
            return "break"

        entry.bind('<Return>', commit)
        entry.bind('<Escape>', cancel)
        entry.bind('<FocusOut>', cancel)
        return "break"

    def _apply_inline_pattern_rename(self, old_name, new_name):
        self.save_to_collection()
        self.collection[new_name] = self.collection.pop(old_name)
        self.order[self.order.index(old_name)] = new_name
        self.current_pattern_name = new_name
        self.refresh_list()
        self.load_pattern_from_collection(new_name)

    # Pattern Creation/Deletion/Modification
    #----------------------------

    def move_pattern(self, direction):
        sel = self.listbox.curselection()
        if not sel or len(sel) > 1: return
        idx = sel[0]
        new_idx = idx + direction
        if 0 <= new_idx < len(self.order):
            self.order[idx], self.order[new_idx] = self.order[new_idx], self.order[idx]
            self.current_pattern_name = self.order[new_idx]
            self.refresh_list()


    def add_pattern(self):
        name = self._ask_custom_string(self.tr('new_patt_title'), self.tr('new_patt_txt'), self.tr('default_pattern_name')+" "+str(len(self.order)+1))
        if name:
            if name not in self.collection:
                self.save_to_collection()
                self.collection[name] = self._get_blank_state()
                self.order.append(name)
                self.current_pattern_name = name
                self.refresh_list()
                self.load_pattern_from_collection(name)
            else:
                messagebox.showerror(self.tr('error'), self.tr('err_exists'))

    def rename_pattern(self):
        old = self.current_pattern_name
        new = self._ask_custom_string(self.tr('rename_patt_title'), self.tr('rename_patt_txt'), old)
        
        if new and new != old:
            if new not in self.collection:
                # Save any pending changes before renaming
                self.save_to_collection()
                # Change the key of the collection dictionary
                self.collection[new] = self.collection.pop(old)
                # Update the list
                self.order[self.order.index(old)] = new
                self.current_pattern_name = new
                self.refresh_list()
                # Reload the new name to check the reindexing
                self.load_pattern_from_collection(new)
            else:
                messagebox.showerror(self.tr('error'), self.tr('err_exists'))

    def duplicate_pattern(self):
        new_name = self._ask_custom_string(self.tr('copy_patt_title'), self.tr('copy_patt_txt'), f"{self.current_pattern_name}_copy")
        if new_name:
            if new_name not in self.collection:
                self.save_to_collection()
                d = self.collection[self.current_pattern_name].copy()
                d["shapes"], d["lines"] = d["shapes"].copy(), d["lines"].copy()
                self.collection[new_name] = d
                self.order.insert(self.order.index(self.current_pattern_name)+1, new_name)
                self.current_pattern_name = new_name
                self.refresh_list()
                self.load_pattern_from_collection(new_name)
            else:
                messagebox.showerror(self.tr('error'), self.tr('err_exists'))

    def delete_pattern(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices: return

        if len(selected_indices) == 1: 
            # Ask confirmation
            confirm = self._ask_custom_confirm(
                self.tr('del_patt_confirm_title'), 
                self.tr('del_patt_confirm_txt').format(self.current_pattern_name)
            )

        else:            
            # Ask confirmation
            confirm = self._ask_custom_confirm(
                self.tr('del_multi_patt_confirm_title'), 
                self.tr('del_multi_patt_confirm_txt').format(len(selected_indices))
            )

        # If OK, go ahead and delete
        if confirm:
            names_to_delete = [self.listbox.get(i) for i in selected_indices]
            for name in names_to_delete:
                self.order.remove(name)
                del self.collection[name]
            if len(self.order) == 0:
                self.order = [self.tr("default_pattern_name")+" 1"]  # List to manage the order of items
                self.collection = {self.tr("default_pattern_name") + " 1": self._get_blank_state()}
            self.load_pattern_from_collection(self.order[0])
            self.refresh_list()


    # Import / Export collection
    #----------------------------
    def export_collection(self):
        self.save_to_collection()
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
        if path:
            out = {"name": self.collection_name, "order": self.order, "data": {}}
            for k, v in self.collection.items():
                v_copy = v.copy()
                v_copy["shapes"] = [[list(pt), t] for pt, t in v["shapes"].items()]
                v_copy["lines"] = [[list(p) for p in line] for line in v["lines"]]
                node_blocked = v.get("blocked_nodes", set())
                v_copy["blocked_nodes"] = [list(pt) for pt in node_blocked]
                out["data"][k] = v_copy
            with open(path, 'w', encoding='utf-8') as f: json.dump(out, f)

    def import_collection(self):
        confirm = self._ask_custom_confirm(
            self.tr('import_confirm_title'), 
            self.tr('import_confirm_txt').format()
            )            
        if confirm:
            path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
            if path:
                with open(path, 'r', encoding='utf-8') as f: data = json.load(f)
                self.collection_name = data.get("name", "Imported")
                self.lbl_coll_name.config(text=self.collection_name)
                self.order = data.get("order", list(data["data"].keys()))
                self.collection = {}
                for k, v in data["data"].items():
                    v["shapes"] = {tuple(pt): t for pt, t in v["shapes"]}
                    v["lines"] = {frozenset(tuple(p) for p in line) for line in v["lines"]}
                    node_blocked = v.get("blocked_nodes", []) # Use empty list if it not exists
                    v["blocked_nodes"] = {tuple(pt) for pt in node_blocked}
                    self.collection[k] = v
                self.load_pattern_from_collection(self.order[0])
                self.refresh_list()

    #--------------------------------------------------------------------------------------------------------
    #  SVG generation Methods
    #--------------------------------------------------------------------------------------------------------

    def batch_export_svg(self):
        self.save_to_collection()
        folder = filedialog.askdirectory()
        if folder:
            for name in self.order:
                self.load_pattern_from_collection(name)
                clean_name=self._clean_filename(self.current_pattern_name)
 
                self._write_svg_file(os.path.join(folder, f"{clean_name}.svg"), crop=self.crop_to_grid.get(), grid=False, lines=self.show_lines.get())

                if self.show_grid.get():
                    self._write_svg_file(os.path.join(folder, f"{clean_name}_grid.svg"), crop=self.crop_to_grid.get(), grid=True, lines=self.show_lines.get())

            messagebox.showinfo(self.tr('export_done_title'), self.tr('export_done_txt'))

    def export_svg(self):
        suggested_name = self._clean_filename(self.current_pattern_name)
        path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG", "*.svg")], initialfile=suggested_name)
        if path:
            base = os.path.splitext(path)[0]
            self._write_svg_file(f"{base}.svg",  crop=self.crop_to_grid.get(), grid=False, lines=self.show_lines.get())

            if self.show_grid.get() and self.show_lines.get():
                self._write_svg_file(f"{base}_grid.svg",  crop=self.crop_to_grid.get(), grid=True, lines=self.show_lines.get())

            messagebox.showinfo(self.tr('export_done_title'), self.tr('export_done_txt'))

    def _write_svg_file(self, filename, crop, grid, lines):
        cell_size = 256 
        GW = self.cols * cell_size
        GH = self.rows * cell_size
        dx = dy = cell_size
        
        grid_type = self.grid_type.get()
        is_isometric = (grid_type == "isometric")

        size = min(dx, dy) * self.shape_size_ratio.get()
        sw_rel = (size / 2) * (self.shape_stroke_pct.get() / 100.0)
        l_sw = cell_size * (self.line_stroke_width.get() / 100.0)
        is_neg = self.negative_mode.get()
        
        if is_isometric:
            # For isometric SVG, calculate the bounds
            # Using cell_size as the isometric "step"
            step = cell_size
            corners = [
                self._grid_to_iso(0, 0, step),
                self._grid_to_iso(self.cols, 0, step),
                self._grid_to_iso(self.cols, self.rows, step),
                self._grid_to_iso(0, self.rows, step)
            ]
            min_x = min(c[0] for c in corners)
            max_x = max(c[0] for c in corners)
            min_y = min(c[1] for c in corners)
            max_y = max(c[1] for c in corners)
            
            iso_w = max_x - min_x
            iso_h = max_y - min_y
            
            if crop:
                vw, vh = iso_w, iso_h
                offset_x = -min_x
                offset_y = -min_y
            else:
                # Add padding
                padding = size / 2
                vw = iso_w + 2 * padding
                vh = iso_h + 2 * padding
                offset_x = padding - min_x
                offset_y = padding - min_y
        else:
            offset_x, offset_y = (0, 0) if crop else (size/2, size/2)
            vw, vh = (GW, GH) if crop else (GW+size, GH+size)

        # Create SVG Frame work
        svg = ['<?xml version="1.0" encoding="UTF-8"?>', f'<svg width="{vw}" height="{vh}" viewBox="0 0 {vw} {vh}" xmlns="http://www.w3.org/2000/svg">']
        if is_neg: svg.append(f'<rect width="{vw}" height="{vh}" fill="{self.color_shapes}" />')

        # Create the Grid if included
        if grid:
            g_col = "#444444" if is_neg else "#eeeeee"
            if is_isometric:
                # Draw isometric grid
                step = cell_size
                # Vertical lines (constant column)
                for i in range(self.cols + 1):
                    points = []
                    for j in range(self.rows + 1):
                        iso_x, iso_y = self._grid_to_iso(i, j, step)
                        points.append(offset_x + iso_x)
                        points.append(offset_y + iso_y)
                    if len(points) >= 4:
                        svg.append(f'<polyline points="{" ".join(f"{points[k]},{points[k+1]}" for k in range(0, len(points), 2))}" fill="none" stroke="{g_col}" stroke-width="1" />')
                
                # Horizontal lines (constant row)
                for j in range(self.rows + 1):
                    points = []
                    for i in range(self.cols + 1):
                        iso_x, iso_y = self._grid_to_iso(i, j, step)
                        points.append(offset_x + iso_x)
                        points.append(offset_y + iso_y)
                    if len(points) >= 4:
                        svg.append(f'<polyline points="{" ".join(f"{points[k]},{points[k+1]}" for k in range(0, len(points), 2))}" fill="none" stroke="{g_col}" stroke-width="1" />')
            else:
                # Draw orthogonal grid
                for i in range(self.cols + 1):
                    x = (i*dx)+offset_x
                    svg.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{vh}" stroke="{g_col}" stroke-width="1" />')
                for j in range(self.rows + 1):
                    y = (j*dy)+offset_y
                    svg.append(f'<line x1="0" y1="{y}" x2="{vw}" y2="{y}" stroke="{g_col}" stroke-width="1" />')

        # Create the lines drawn if included
        if lines:
            step = cell_size
            for line in self.pattern_lines:
                pts = list(line)
                if is_isometric:
                    iso_x1, iso_y1 = self._grid_to_iso(pts[0][0], pts[0][1], step)
                    iso_x2, iso_y2 = self._grid_to_iso(pts[1][0], pts[1][1], step)
                    x1, y1 = offset_x + iso_x1, offset_y + iso_y1
                    x2, y2 = offset_x + iso_x2, offset_y + iso_y2
                else:
                    x1, y1 = (pts[0][0]*dx)+offset_x, (pts[0][1]*dy)+offset_y
                    x2, y2 = (pts[1][0]*dx)+offset_x, (pts[1][1]*dy)+offset_y
                svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{self.color_lines}" stroke-width="{l_sw}" stroke-linecap="round" />')
            
            if hasattr(self, 'blocked_nodes'):
                r_point = l_sw / 2
                step = cell_size
                for (c, r_idx) in self.blocked_nodes:
                    if is_isometric:
                        iso_x, iso_y = self._grid_to_iso(c, r_idx, step)
                        px = offset_x + iso_x
                        py = offset_y + iso_y
                    else:
                        px = (c * dx) + offset_x
                        py = (r_idx * dy) + offset_y
                    svg.append(f'<circle cx="{px}" cy="{py}" r="{r_point}" fill="{self.color_lines}" />')

        # Create the shapes
        #   - Get the family of shape to use
        fam = self.collection[self.current_pattern_name].get('tool', 'circle')
        
        #   - List of point of a circle contained in the generated box (allowing proper cropping)
        def gen_circle_pts(cx, cy, r, cw=True):
            s = 60
            # Limiting the points to the viewing box
            return "L ".join([f"{max(0,min(vw,cx+r*math.cos(2*math.pi*i/s))):.2f},{max(0,min(vh,cy+r*math.sin(2*math.pi*i/s))):.2f}" for i in (range(s+1) if cw else range(s,-1,-1))])
        
        shape_color = "white" if is_neg else self.color_shapes
        
        #   - Prep index 
        index_path_data = ""
        target_node = (0, self.rows // 2 if self.rows % 2 == 0 else (self.rows - 1) // 2)
        if self.show_index.get():
            step = cell_size
            if is_isometric:
                iso_x, iso_y = self._grid_to_iso(0, target_node[1], step)
                center_x = offset_x + iso_x
                center_y = offset_y + iso_y
            else:
                center_x = offset_x
                center_y = offset_y + target_node[1] * dy
            
            idx_pts = self._get_index_triangle_points(center_x, center_y, dy, size)
            safe_pts = []
            # Forces points to stay within the viewing box to avoid the shape to overflow on cropped version
            for px, py in idx_pts: 
                clipped_x = max(0, min(vw, px))
                clipped_y = max(0, min(vh, py))
                safe_pts.append(f"{clipped_x:.2f},{clipped_y:.2f}")
            # Create SVG path for the index
            index_path_data = f"M {safe_pts[0]} L {safe_pts[1]} L {safe_pts[2]} Z"

        if self.show_shapes.get():
            for (c, r), s_type in self.pattern_shapes.items():
                step = cell_size
                if is_isometric:
                    iso_x, iso_y = self._grid_to_iso(c, r, step)
                    x, y = offset_x + iso_x, offset_y + iso_y
                else:
                    x, y = (c*dx)+offset_x, (r*dy)+offset_y
                
                if fam == "circle":
                    ro = size/2
                    # Starting point (M) shall be included in the viewing box
                    start_x = max(0, min(vw, x + ro))
                    d = f"M {start_x},{max(0,min(vh,y))} {gen_circle_pts(x,y,ro,True)} Z"
                    if s_type == "outline":
                        ri = max(0, ro-sw_rel)
                        start_xi = max(0, min(vw, x + ri))
                        d += f" M {start_xi},{max(0,min(vh,y))} {gen_circle_pts(x,y,ri,False)} Z"           
                else:
                    do = size/2
                    # Squares are binded by the viewing box to allow proper cropping
                    x1, y1 = max(0, min(vw, x-do)), max(0, min(vh, y-do))
                    x2, y2 = max(0, min(vw, x+do)), max(0, min(vh, y+do)) 
                    d = f"M {x1},{y1} H {x2} V {y2} H {x1} Z"
                    if s_type == "outline":
                        di = max(0, do-sw_rel)
                        # Interior Squares are also binded by the viewing box to allow proper cropping
                        ix1, iy1 = max(0, min(vw, x-di)), max(0, min(vh, y-di))
                        ix2, iy2 = max(0, min(vw, x+di)), max(0, min(vh, y+di))
                        # Invert tracing of interior to allow le fill-rule:evenodd
                        d += f" M {ix1},{iy1} V {iy2} H {ix2} V {iy1} Z"
                
                if (c, r) == target_node and index_path_data and self.color_shapes == self.color_index:
                    d += f" {index_path_data}"
                    index_path_data = "" #delete index_path to not add it on next nodes
                
                # Create the SVG path
                svg.append(f'<path d="{d}" fill="{shape_color}" fill-rule="evenodd" />')
        
        if index_path_data:
            # If index path was not included in any shape, add it separately on top of the shapes
            svg.append(f'<path d="{index_path_data}" fill="{self.color_index}" fill-rule="evenodd" />')

        # Complete the SVG and write it
        svg.append('</svg>')
        with open(filename, "w", encoding="utf-8") as f: f.write("\n".join(svg))

    #--------------------------------------------------------------------------------------------------------
    #  Canvas Methods
    #--------------------------------------------------------------------------------------------------------

    def draw_canvas(self):
        self.canvas.delete("all")
        t_pct = self.shape_stroke_pct.get() / 100.0
        l_sw = self.line_stroke_width.get()
        
        # Use same step for X and Y 
        step, _ = self.get_coords()
        if step <= 0: return
        
        grid_type = self.grid_type.get()
        is_isometric = (grid_type == "isometric")

        # Computation of available space to center the grid within the canvas
        available_w = self.canvas.winfo_width()
        available_h = self.canvas.winfo_height()
        
        # For isometric, calculate bounding box differently
        if is_isometric:
            # Calculate the bounds of the isometric grid
            corners = [
                self._grid_to_iso(0, 0, step),
                self._grid_to_iso(self.cols, 0, step),
                self._grid_to_iso(self.cols, self.rows, step),
                self._grid_to_iso(0, self.rows, step)
            ]
            min_x = min(c[0] for c in corners)
            max_x = max(c[0] for c in corners)
            min_y = min(c[1] for c in corners)
            max_y = max(c[1] for c in corners)
            
            iso_w = max_x - min_x
            iso_h = max_y - min_y
            
            offset_x = (available_w - iso_w) / 2 - min_x
            offset_y = (available_h - iso_h) / 2 - min_y
            dx = dy = step
        else:
            # Orthogonal grid
            dx = dy = step
            grid_w = self.cols * dx
            grid_h = self.rows * dy
            
            offset_x = (available_w - grid_w) / 2
            offset_y = (available_h - grid_h) / 2

        # Negative mode
        is_neg = self.negative_mode.get()
        if is_neg:
            # fill all visible canvas (0,0 à cw,ch)
            self.canvas.create_rectangle(0, 0, available_w, available_h, fill=self.color_shapes, outline="")
            # fill background color of the canvas to avoid white flash on the display
            self.canvas.config(bg=self.color_shapes)
        else:
            self.canvas.config(bg="white")

        # Create the Grid if included
        if self.show_grid.get():
            g_col = "#444" if is_neg else "#eee"
            
            if is_isometric:
                # Draw isometric grid
                # Draw vertical lines (constant column)
                for i in range(self.cols + 1):
                    points = []
                    for j in range(self.rows + 1):
                        iso_x, iso_y = self._grid_to_iso(i, j, step)
                        points.append(offset_x + iso_x)
                        points.append(offset_y + iso_y)
                    if len(points) >= 4:
                        self.canvas.create_line(*points, fill=g_col)
                
                # Draw horizontal lines (constant row)
                for j in range(self.rows + 1):
                    points = []
                    for i in range(self.cols + 1):
                        iso_x, iso_y = self._grid_to_iso(i, j, step)
                        points.append(offset_x + iso_x)
                        points.append(offset_y + iso_y)
                    if len(points) >= 4:
                        self.canvas.create_line(*points, fill=g_col)
            else:
                # Draw orthogonal grid
                for i in range(self.cols + 1):
                    x = offset_x + i * dx
                    self.canvas.create_line(x, offset_y, x, offset_y + self.rows * dy, fill=g_col)
                for j in range(self.rows + 1):
                    y = offset_y + j * dy
                    self.canvas.create_line(offset_x, y, offset_x + self.cols * dx, y, fill=g_col)

        # Display cropping border if enabled
        if self.crop_to_grid.get():
            if is_isometric:
                # Draw isometric cropping border
                corners = [
                    (offset_x + self._grid_to_iso(0, 0, step)[0], offset_y + self._grid_to_iso(0, 0, step)[1]),
                    (offset_x + self._grid_to_iso(self.cols, 0, step)[0], offset_y + self._grid_to_iso(self.cols, 0, step)[1]),
                    (offset_x + self._grid_to_iso(self.cols, self.rows, step)[0], offset_y + self._grid_to_iso(self.cols, self.rows, step)[1]),
                    (offset_x + self._grid_to_iso(0, self.rows, step)[0], offset_y + self._grid_to_iso(0, self.rows, step)[1])
                ]
                for i in range(4):
                    x1, y1 = corners[i]
                    x2, y2 = corners[(i + 1) % 4]
                    self.canvas.create_line(x1, y1, x2, y2, fill="#00d2ff", width=2, dash=(4, 4))
            else:
                # Draw orthogonal cropping border
                self.canvas.create_rectangle(offset_x, offset_y, offset_x+self.cols*dx, offset_y+self.rows*dy, outline="#00d2ff", width=2, dash=(4,4))

        # Create the Drawing/Lines if included and line width not 0
        if self.show_lines.get() and l_sw != 0:
            for line in self.pattern_lines:
                pts = list(line)
                if is_isometric:
                    iso_x1, iso_y1 = self._grid_to_iso(pts[0][0], pts[0][1], step)
                    iso_x2, iso_y2 = self._grid_to_iso(pts[1][0], pts[1][1], step)
                    x1, y1 = offset_x + iso_x1, offset_y + iso_y1
                    x2, y2 = offset_x + iso_x2, offset_y + iso_y2
                else:
                    x1, y1 = offset_x + pts[0][0] * dx, offset_y + pts[0][1] * dy
                    x2, y2 = offset_x + pts[1][0] * dx, offset_y + pts[1][1] * dy
                self.canvas.create_line(x1, y1, x2, y2, fill=self.color_lines, width=l_sw, capstyle=tk.ROUND)

            if hasattr(self, 'blocked_nodes'):
                # Diameter = line width
                r = l_sw / 2
                for (c, r_idx) in self.blocked_nodes:
                    if is_isometric:
                        iso_x, iso_y = self._grid_to_iso(c, r_idx, step)
                        px = offset_x + iso_x
                        py = offset_y + iso_y
                    else:
                        px = offset_x + c * dx
                        py = offset_y + r_idx * dy
                    self.canvas.create_oval(px - r, py - r, px + r, py + r, fill=self.color_lines, outline="")

        # Display line start point
        if self.line_start_point:
            if is_isometric:
                iso_x, iso_y = self._grid_to_iso(self.line_start_point[0], self.line_start_point[1], step)
                sx, sy = offset_x + iso_x, offset_y + iso_y
            else:
                sx = offset_x + self.line_start_point[0] * dx
                sy = offset_y + self.line_start_point[1] * dy
            self.canvas.create_oval(sx - 6, sy - 6, sx + 6, sy + 6, outline="#ff7675", width=3)
        
        # Display shapes if enabled
        if self.show_shapes.get():
            # Create the Shapes
            base = min(dx, dy) * self.shape_size_ratio.get()
            fill = "white" if is_neg else self.color_shapes

            # - Use the shape tool stored for the current pattern independently of the active tool
            #   to be able to render the shapes if the active tool is the drawing one ('line')
            fam = self.collection[self.current_pattern_name].get('tool', 'circle')
            for (c, r), t in self.pattern_shapes.items():
                if is_isometric:
                    iso_x, iso_y = self._grid_to_iso(c, r, step)
                    x, y = offset_x + iso_x, offset_y + iso_y
                else:
                    x = offset_x + c * dx
                    y = offset_y + r * dy
                
                re = base / 2
                if t == "full": self._draw_shape_canvas(x, y, re, fam, fill, "", 0)
                else:
                    sw = re * t_pct
                    ir = max(0, re - (sw / 2))
                    self._draw_shape_canvas(x, y, ir, fam, "", fill, sw)
        
        # Create the Index if enabled
        if self.show_index.get():
            base_s = min(dx, dy) * self.shape_size_ratio.get()
            target_row = self.rows // 2 if self.rows % 2 == 0 else (self.rows - 1) // 2
            
            if is_isometric:
                iso_x, iso_y = self._grid_to_iso(0, target_row, step)
                center_x = offset_x + iso_x
                center_y = offset_y + iso_y
            else:
                center_x = offset_x
                center_y = offset_y + target_row * dy
            
            pts = self._get_index_triangle_points(center_x, center_y, dy, base_s)
            
            # Adapt the color of the index if node is occupied and index color is the one of shapes           
            is_node_occupied = (0, target_row) in self.pattern_shapes and self.show_shapes.get()
            if self.color_index == self.color_shapes:
                if is_node_occupied and self.pattern_shapes[(0, target_row)] == "full":
                    t_fill = self.color_shapes if is_neg else "white"
                else:
                    t_fill = "white" if is_neg else self.color_shapes
            else:
                t_fill = self.color_index
            self.canvas.create_polygon(pts, fill=t_fill, outline="")

    def clear_all(self):
        confirm = self._ask_custom_confirm(
            self.tr('clear_all_confirm_title'), 
            self.tr('clear_all_confirm_txt')
            )            
        if confirm:
            self.pattern_shapes, self.pattern_lines, self.blocked_nodes, self.line_start_point = {}, set(), set(), None
            self.save_to_collection(); self.draw_canvas()
        return confirm

    def clear_shapes(self): 
        self.pattern_shapes = {}
        self.save_to_collection(); self.draw_canvas()

    def _draw_shape_canvas(self, x, y, r, family, fill, outline, width):
        if family == "circle": self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=fill, outline=outline, width=width)
        else: self.canvas.create_rectangle(x-r, y-r, x+r, y+r, fill=fill, outline=outline, width=width)

    def _on_canvas_click(self, event):
        # Use same step for X and Y 
        step, _ = self.get_coords()
        if step <= 0: return

        # Re-compute the padding and offset
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        grid_type = self.grid_type.get()
        is_isometric = (grid_type == "isometric")

        if is_isometric:
            # Calculate offset for isometric grid
            corners = [
                self._grid_to_iso(0, 0, step),
                self._grid_to_iso(self.cols, 0, step),
                self._grid_to_iso(self.cols, self.rows, step),
                self._grid_to_iso(0, self.rows, step)
            ]
            min_x = min(c[0] for c in corners)
            max_x = max(c[0] for c in corners)
            min_y = min(c[1] for c in corners)
            max_y = max(c[1] for c in corners)
            
            iso_w = max_x - min_x
            iso_h = max_y - min_y
            
            offset_x = (cw - iso_w) / 2 - min_x
            offset_y = (ch - iso_h) / 2 - min_y
            
            # Convert screen coordinates to isometric coordinates
            iso_x = event.x - offset_x
            iso_y = event.y - offset_y
            
            # Convert isometric coordinates to grid coordinates
            col, row = self._iso_to_grid(iso_x, iso_y, step)
        else:
            # Orthogonal grid
            dx = dy = step
            grid_w = self.cols * dx
            grid_h = self.rows * dy
            offset_x = (cw - grid_w) / 2
            offset_y = (ch - grid_h) / 2
            
            # Convert Mouse position to Grid position (col, row)
            col = round((event.x - offset_x) / dx)
            row = round((event.y - offset_y) / dy)

        # Round to nearest integer for grid position
        col = round(col)
        row = round(row)

        # Check click is within Grid
        if 0 <= col <= self.cols and 0 <= row <= self.rows:
            tool = self.active_tool.get()
            key = (col, row)
            if tool == "line":
                # Selected point is a blocking one
                if key in self.blocked_nodes:
                    self.blocked_nodes.remove(key)
                    self.line_start_point = None
                # First selection of a Node
                elif self.line_start_point is None:
                    self.line_start_point = (col, row)
                # Already selected node
                elif self.line_start_point == key:
                    self.blocked_nodes.add(key)
                    self.line_start_point = None
                # New node after selecting a first one
                else:
                    lk = frozenset({self.line_start_point, (col, row)})
                    if lk in self.pattern_lines:
                        self.pattern_lines.remove(lk)
                    else:
                        self.pattern_lines.add(lk)
                    self.line_start_point = None
            else:
                self.line_start_point = None
                # For shapes, toggle the content
                key = (col, row)
                if key not in self.pattern_shapes:
                    self.pattern_shapes[key] = "full"
                elif self.pattern_shapes[key] == "full" and self.use_outlined_shape.get():
                    self.pattern_shapes[key] = "outline"
                else:
                    del self.pattern_shapes[key]

        # Save and refresh the canvas
        self.save_to_collection()
        self.draw_canvas()

    def get_coords(self):
        # Get total available space
        self.canvas.update()
        available_w = self.canvas.winfo_width() - (2 * self.padding)
        available_h = self.canvas.winfo_height() - (2 * self.padding)      
        if available_w <= 0 or available_h <= 0:
            return 0, 0

        if self.grid_type.get() == "isometric":
            # For isometric grid: vertical lines stay vertical, horizontal lines skewed at 30°
            # Bounding box: width = cols * √3/2 * step
            #              height = rows * step + cols * 0.5 * step
            sqrt3 = math.sqrt(3)
            max_step_w = available_w / (self.cols * sqrt3 / 2)
            max_step_h = available_h / (self.rows + self.cols * 0.5)
            step = min(max_step_w, max_step_h)
        else:
            # Compute max size of cells for orthogonal grid
            max_dx = available_w / self.cols
            max_dy = available_h / self.rows
            
            # Pick the minimum of the 2 to get a 1:1 ratio for each cells
            step = min(max_dx, max_dy)
        
        return step, step

    def _grid_to_iso(self, col, row, step):
        """Convert grid coordinates (col, row) to isometric screen coordinates"""
        # Isometric projection: vertical lines stay vertical
        # Horizontal axis rotated by 30°, creating proper isometric depth effect
        # iso_x = col * cos(30°) = col * √3/2 * step
        # iso_y = row * step + col * sin(30°) = row * step + col * 0.5 * step
        iso_x = col * step * math.sqrt(3) / 2
        iso_y = row * step + col * step * 0.5
        return iso_x, iso_y

    def _iso_to_grid(self, iso_x, iso_y, step):
        """Convert isometric screen coordinates back to grid coordinates (col, row)"""
        # Inverse transformation
        sqrt3 = math.sqrt(3)
        col = iso_x * 2 / (step * sqrt3)
        row = (iso_y - col * step * 0.5) / step
        return col, row

    def update_grid_size(self):
        try: 
            if (int(self.ent_cols.get()) >= 1 and int(self.ent_rows.get()) >= 1):
                new_cols = int(self.ent_cols.get())
                new_rows = int(self.ent_rows.get())
                
                # Grid is being reduced
                if (new_cols < self.cols or new_rows < self.rows):
                    # Check if any elements are in the removed area
                    elements_in_removed_area = self._check_elements_in_removed_area(new_cols, new_rows)
                    
                    if elements_in_removed_area:
                        # Elements exist in the removed area, ask for confirmation
                        confirm = self._ask_custom_confirm(
                            self.tr('resize_confirm_title'), 
                            self.tr('resize_confirm_txt')
                        )
                        
                        if confirm:
                            # Remove only elements that are outside the new grid bounds
                            self._remove_elements_outside_bounds(new_cols, new_rows)
                            self.cols, self.rows = new_cols, new_rows
                            self.show_grid.set(True) # Force grid display to help user visualize the new bounds after resizing
                            self.save_to_collection(); self.draw_canvas()
                        return
                
                # No elements in removed area, just update the grid
                self.cols, self.rows = new_cols, new_rows
                self.show_grid.set(True) # Force grid display to help user visualize the new bounds after resizing
                self.save_to_collection(); self.draw_canvas()
                return
            else:
                messagebox.showerror(self.tr('error'), self.tr('err_invalid_input'))
                return

        except:
            messagebox.showerror(self.tr('error'), self.tr('err_invalid_input'))
            return

    def _check_elements_in_removed_area(self, new_cols, new_rows):
        """Check if any shapes, lines, or blocked nodes are in the area being removed."""
        # Check shapes
        for (c, r) in self.pattern_shapes.keys():
            if c > new_cols or r > new_rows:
                return True
        
        # Check blocked nodes
        for (c, r) in self.blocked_nodes:
            if c > new_cols or r > new_rows:
                return True
        
        # Check lines
        for line in self.pattern_lines:
            pts = list(line)
            for (c, r) in pts:
                if c > new_cols or r > new_rows:
                    return True
        
        return False

    def _remove_elements_outside_bounds(self, new_cols, new_rows):
        """Remove shapes, lines, and blocked nodes that are outside the new grid bounds."""
        # Remove shapes outside bounds
        shapes_to_remove = [key for key in self.pattern_shapes.keys() if key[0] > new_cols or key[1] > new_rows]
        for key in shapes_to_remove:
            del self.pattern_shapes[key]
        
        # Remove blocked nodes outside bounds
        self.blocked_nodes = {(c, r) for (c, r) in self.blocked_nodes if c <= new_cols and r <= new_rows}
        
        # Remove lines outside bounds
        lines_to_remove = [line for line in self.pattern_lines 
                          for (c, r) in list(line) if c > new_cols or r > new_rows]
        for line in lines_to_remove:
            self.pattern_lines.discard(line)


    #--------------------------------------------------------------------------------------------------------
    #  Transformation Helper Methods
    #--------------------------------------------------------------------------------------------------------
    
    def _ask_transformation_params(self, title_key, dim_prompt_key, op_prompt_key=None, value_prompt_key=None, value_default=None, min_val=None, max_val=None, sym=False):
        """Combined dialog for transformation parameters: dimensions, operation, and/or integer values"""
        self.root.update_idletasks()
        result = {"dimensions": {"x": False, "y": False}, "operation": None, "values": {"x": None, "y": None}}
        
        # Calculate dialog height based on what's needed
        height = 130  # Base height for dimension checkboxes
        if op_prompt_key:
            height += 60
        if value_prompt_key:
            height += 80
        
        dialog = tk.Toplevel(self.root)
        dialog.title(self.tr(title_key))
        dialog.geometry(f"340x{height}")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 170
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (height // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Dimension selection (checkboxes to allow both)
        tk.Label(dialog, text=self.tr(dim_prompt_key), anchor="w", justify=tk.LEFT, font=('Arial', 9, 'bold')).pack(fill=tk.X, padx=20, pady=(15, 5))
        
        dim_x_var = tk.BooleanVar(value=True)
        dim_y_var = tk.BooleanVar(value=True)
        f_dim = tk.Frame(dialog)
        f_dim.pack(fill=tk.X, padx=20, pady=5)
        tk.Checkbutton(f_dim, text=(self.tr('axis_x') if sym else self.tr('dim_x')), variable=dim_x_var).pack(side=tk.LEFT, padx=(0, 20))
        tk.Checkbutton(f_dim, text=(self.tr('axis_y') if sym else self.tr('dim_y')), variable=dim_y_var).pack(side=tk.LEFT)
        
        # Operation selection (if needed)
        op_var = tk.StringVar(value="multiply")
        if op_prompt_key:
            tk.Label(dialog, text=self.tr(op_prompt_key), anchor="w", justify=tk.LEFT, font=('Arial', 9)).pack(fill=tk.X, padx=20, pady=(10, 5))
            f_op = tk.Frame(dialog)
            f_op.pack(fill=tk.X, padx=20, pady=5)
            tk.Radiobutton(f_op, text=self.tr('op_multiply'), variable=op_var, value="multiply").pack(side=tk.LEFT, padx=(0, 20))
            tk.Radiobutton(f_op, text=self.tr('op_divide'), variable=op_var, value="divide").pack(side=tk.LEFT)
        
        # Integer value input (if needed) - separate entries for X and Y
        value_entry_x = None
        value_entry_y = None
        if value_prompt_key:
            tk.Label(dialog, text=self.tr(value_prompt_key), anchor="w", justify=tk.LEFT, font=('Arial', 9)).pack(fill=tk.X, padx=20, pady=(10, 5))
            
            # X and Y value fields
            f_values = tk.Frame(dialog)
            f_values.pack(fill=tk.X, padx=20, pady=5)
            f_values.grid_columnconfigure(1, weight=1)
            f_values.grid_columnconfigure(3, weight=1)
            
            tk.Label(f_values, text=self.tr('dim_x')+": ", font=('Arial', 8)).grid(row=0, column=0, sticky="w", padx=(0, 5))
            value_entry_x = tk.Entry(f_values, width=8)
            value_entry_x.insert(0, str(value_default if value_default is not None else 1))
            value_entry_x.grid(row=0, column=1, sticky="ew", padx=(0, 15))
            
            tk.Label(f_values, text=self.tr('dim_y')+": ", font=('Arial', 8)).grid(row=0, column=2, sticky="w", padx=(0, 5))
            value_entry_y = tk.Entry(f_values, width=8)
            value_entry_y.insert(0, str(value_default if value_default is not None else 1))
            value_entry_y.grid(row=0, column=3, sticky="ew")
            
            value_entry_x.focus_set()
        
        def validate():
            if not dim_x_var.get() and not dim_y_var.get():
                messagebox.showerror(self.tr('error'), "Please select at least one dimension")
                return
            
            result["dimensions"]["x"] = dim_x_var.get()
            result["dimensions"]["y"] = dim_y_var.get()
            result["operation"] = op_var.get() if op_prompt_key else None
            
            if value_prompt_key:
                try:
                    if dim_x_var.get():
                        val_x = int(value_entry_x.get().strip())
                        if min_val is not None and val_x < min_val:
                            messagebox.showerror(self.tr('error'), self.tr('err_value_too_small').format(val_x, 'X', min_val))
                            return
                        if max_val is not None and val_x > max_val:
                            messagebox.showerror(self.tr('error'), self.tr('err_value_too_large').format(val_x, 'X', max_val))
                            return
                        result["values"]["x"] = val_x
                    
                    if dim_y_var.get():
                        val_y = int(value_entry_y.get().strip())
                        if min_val is not None and val_y < min_val:
                            messagebox.showerror(self.tr('error'), self.tr('err_value_too_small').format(val_y, 'Y', min_val))
                            return
                        if max_val is not None and val_y > max_val:
                            messagebox.showerror(self.tr('error'), self.tr('err_value_too_large').format(val_y, 'Y', max_val))
                            return
                        result["values"]["y"] = val_y
                except ValueError:
                    messagebox.showerror(self.tr('error'), self.tr('err_invalid_input'))
                    return
            
            dialog.destroy()
        
        f_btns = tk.Frame(dialog)
        f_btns.pack(fill=tk.X, padx=20, pady=15)
        tk.Button(f_btns, text=self.tr('btn_ok'), width=9, command=validate, default=tk.ACTIVE).pack(side=tk.RIGHT, padx=(5, 0))
        tk.Button(f_btns, text=self.tr('btn_cancel'), width=9, command=dialog.destroy).pack(side=tk.RIGHT)
        
        dialog.bind("<Return>", lambda e: validate())
        dialog.bind("<Escape>", lambda e: dialog.destroy())
        
        self.root.wait_window(dialog)
        return result["dimensions"], result["operation"], result["values"]

    #--------------------------------------------------------------------------------------------------------
    #  Transformation Methods
    #--------------------------------------------------------------------------------------------------------
    
    def _apply_transform_to_multi(self, transform_name):
        """Helper to apply transformation to multiple selected patterns"""
        selected = self.listbox.curselection()
        if len(selected) <= 1: return False
        
        saved_name = self.current_pattern_name
        for idx in selected:
            self.load_pattern_from_collection(self.listbox.get(idx))
            self._apply_single_transform(transform_name)
        self.load_pattern_from_collection(saved_name)
        return True
    
    def _apply_single_transform(self, transform_name):
        """Apply a single transformation to current pattern"""
        if transform_name == "scale": self._do_transform_scale()
        elif transform_name == "shift": self._do_transform_shift()
        elif transform_name == "copy_shift": self._do_transform_copy_shift()
        elif transform_name == "symmetry": self._do_transform_symmetry()
    
    def transform_scale(self):
        """Scale the pattern by multiplying or dividing coordinates"""
    
        # Grab the selected patterns before losing mouse focus from the listbox to be able to apply the transformation on multiple patterns at once if needed
        selected = self.listbox.curselection()

        dimensions, operation, factors = self._ask_transformation_params(
            'scale_title', 'scale_dim_prompt', 'scale_op_prompt', 'scale_factor_prompt',
            value_default=1, min_val=1
        )
        
        if not any(dimensions.values()):  # Check if at least one dimension was selected
            return
        
        if len(selected) > 1:  # Multiple patterns selected
            saved_name = self.current_pattern_name
            for idx in selected:
                self.load_pattern_from_collection(self.listbox.get(idx))
                self._do_scale(dimensions, operation, factors)
            self.load_pattern_from_collection(saved_name)
            messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
            return
        
        self._do_scale(dimensions, operation, factors)
        messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
    
    def _do_scale(self, dimensions, operation, factors):
        """Apply scale transformation to current pattern"""
        # Validate factors against grid sizes
        if dimensions["x"] and factors["x"] is not None:
            if operation == "divide" and factors["x"] > self.cols:
                messagebox.showerror(self.tr('error'), self.tr('err_factor_too_large').format(factors['x'], 'X', self.cols))
                return
        if dimensions["y"] and factors["y"] is not None:
            if operation == "divide" and factors["y"] > self.rows:
                messagebox.showerror(self.tr('error'), self.tr('err_factor_too_large').format(factors['y'], 'Y', self.rows))
                return
        
        self.save_to_collection()
        factor_x = factors["x"] if dimensions["x"] and factors["x"] is not None else 1
        factor_y = factors["y"] if dimensions["y"] and factors["y"] is not None else 1
        new_shapes, new_lines, new_blocked = {}, set(), set()
        
        if operation == "multiply":
            if dimensions["x"]: self.cols *= factor_x
            if dimensions["y"]: self.rows *= factor_y
            for (c, r), shape_type in self.pattern_shapes.items():
                new_shapes[(c * factor_x if dimensions["x"] else c, r * factor_y if dimensions["y"] else r)] = shape_type
            for line in self.pattern_lines:
                pts = [(c * factor_x if dimensions["x"] else c, r * factor_y if dimensions["y"] else r) for c, r in line]
                new_lines.add(frozenset({tuple(pts[0]), tuple(pts[1])}))
            for (c, r) in self.blocked_nodes:
                new_blocked.add((c * factor_x if dimensions["x"] else c, r * factor_y if dimensions["y"] else r))
        else:  # divide
            for (c, r), shape_type in self.pattern_shapes.items():
                new_shapes[(c // factor_x if dimensions["x"] else c, r // factor_y if dimensions["y"] else r)] = shape_type
            for line in self.pattern_lines:
                pts = [(c // factor_x if dimensions["x"] else c, r // factor_y if dimensions["y"] else r) for c, r in line]
                if pts[0] != pts[1]:
                    new_lines.add(frozenset({tuple(pts[0]), tuple(pts[1])}))
            for (c, r) in self.blocked_nodes:
                new_blocked.add((c // factor_x if dimensions["x"] else c, r // factor_y if dimensions["y"] else r))
            if dimensions["x"]: self.cols = max(1, self.cols // factor_x)
            if dimensions["y"]: self.rows = max(1, self.rows // factor_y)
        
        self.pattern_shapes = new_shapes
        self.pattern_lines = new_lines
        self.blocked_nodes = new_blocked
        self.ent_cols.delete(0, tk.END); self.ent_cols.insert(0, str(self.cols))
        self.ent_rows.delete(0, tk.END); self.ent_rows.insert(0, str(self.rows))
        self.save_to_collection()
        self.draw_canvas()

    
    def transform_shift(self):
        """Shift shapes and lines in a given dimension"""

        # Grab the selected patterns before losing mouse focus from the listbox to be able to apply the transformation on multiple patterns at once if needed
        selected = self.listbox.curselection()

        dimensions, _, steps = self._ask_transformation_params(
            'shift_title', 'shift_dim_prompt', value_prompt_key='shift_step_prompt', value_default=0
        )
        
        if not any(dimensions.values()) or (steps["x"] is None and steps["y"] is None):
            return
        
        if len(selected) > 1:  # Multiple patterns selected
            saved_name = self.current_pattern_name
            for idx in selected:
                self.load_pattern_from_collection(self.listbox.get(idx))
                self._do_shift(dimensions, steps)
            self.load_pattern_from_collection(saved_name)
            messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
            return
        
        self._do_shift(dimensions, steps)
        messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
    
    def _do_shift(self, dimensions, steps):
        """Apply shift transformation to current pattern"""
        # Check if data will be lost for negative shifts
        if steps["x"] < 0 or steps["y"] < 0:
            will_lose_data = any((dimensions["x"] and c + steps["x"] < 0) or (dimensions["y"] and r + steps["y"] < 0) 
                                 for c, r in self.pattern_shapes.keys())
            if not will_lose_data:
                for line in self.pattern_lines:
                    if any((dimensions["x"] and c + steps["x"] < 0) or (dimensions["y"] and r + steps["y"] < 0) for c, r in line):
                        will_lose_data = True
                        break
            if will_lose_data and not self._ask_custom_confirm('shift_confirm_title', 'shift_confirm_txt'):
                return
        
        self.save_to_collection()
        for dimension in ["x", "y"]:
            if dimensions[dimension]:
                new_shapes = {}
                for (c, r), shape_type in self.pattern_shapes.items():
                    nc = (c + steps["x"], r) if dimension == "x" else (c, r + steps["y"])
                    if nc[0] >= 0 and nc[1] >= 0:
                        new_shapes[nc] = shape_type
                
                new_lines = set()
                for line in self.pattern_lines:
                    pts = [(c + steps["x"], r) if dimension == "x" else (c, r + steps["y"]) for c, r in line]
                    if all(p[0] >= 0 and p[1] >= 0 for p in pts):
                        new_lines.add(frozenset({tuple(pts[0]), tuple(pts[1])}))
                
                new_blocked = set()
                for (c, r) in self.blocked_nodes:
                    nc = (c + steps["x"], r) if dimension == "x" else (c, r + steps["y"])
                    if nc[0] >= 0 and nc[1] >= 0:
                        new_blocked.add(nc)
                
                if steps["x"] > 0 or steps["y"] > 0:
                    if dimension == "x": self.cols += steps["x"]
                    else: self.rows += steps["y"]
                
                self.pattern_shapes = new_shapes
                self.pattern_lines = new_lines
                self.blocked_nodes = new_blocked
                self.ent_cols.delete(0, tk.END); self.ent_cols.insert(0, str(self.cols))
                self.ent_rows.delete(0, tk.END); self.ent_rows.insert(0, str(self.rows))
                self.save_to_collection()
                self.draw_canvas()

    
    def transform_copy_shift(self):
        """Copy and shift pattern in a dimension, doubling the grid"""

        dimensions, _, _ = self._ask_transformation_params(
            'copy_shift_title', 'copy_shift_dim_prompt'
        )
        
        if not any(dimensions.values()):
            return
        
        selected = self.listbox.curselection()
        if len(selected) > 1:  # Multiple patterns selected
            saved_name = self.current_pattern_name
            for idx in selected:
                self.load_pattern_from_collection(self.listbox.get(idx))
                self._do_copy_shift(dimensions)
            self.load_pattern_from_collection(saved_name)
            messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
            return
        
        self._do_copy_shift(dimensions)
        messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
    
    def _do_copy_shift(self, dimensions):
        """Apply copy & shift transformation to current pattern"""
        self.save_to_collection()
        shift_x = self.cols if dimensions["x"] else 0
        shift_y = self.rows if dimensions["y"] else 0
        new_cols = self.cols * 2 if dimensions["x"] else self.cols
        new_rows = self.rows * 2 if dimensions["y"] else self.rows
        
        new_shapes = self.pattern_shapes.copy()
        for (c, r), shape_type in self.pattern_shapes.items():
            new_shapes[(c + shift_x, r + shift_y)] = shape_type
        
        new_lines = self.pattern_lines.copy()
        for line in self.pattern_lines:
            pts = [(c + shift_x, r + shift_y) for c, r in line]
            new_lines.add(frozenset({tuple(pts[0]), tuple(pts[1])}))
        
        new_blocked = self.blocked_nodes.copy()
        for (c, r) in self.blocked_nodes:
            new_blocked.add((c + shift_x, r + shift_y))
        
        self.cols, self.rows = new_cols, new_rows
        self.pattern_shapes, self.pattern_lines, self.blocked_nodes = new_shapes, new_lines, new_blocked
        self.ent_cols.delete(0, tk.END); self.ent_cols.insert(0, str(self.cols))
        self.ent_rows.delete(0, tk.END); self.ent_rows.insert(0, str(self.rows))
        self.save_to_collection()
        self.draw_canvas()

    
    def transform_symmetry(self):
        """Mirror pattern with axial symmetry"""

        dimensions, _, _ = self._ask_transformation_params(
            'symmetry_title', 'symmetry_dim_prompt', sym=True
        )
        
        if not any(dimensions.values()):
            return
        
        selected = self.listbox.curselection()
        if len(selected) > 1:  # Multiple patterns selected
            saved_name = self.current_pattern_name
            for idx in selected:
                self.load_pattern_from_collection(self.listbox.get(idx))
                self._do_symmetry(dimensions)
            self.load_pattern_from_collection(saved_name)
            messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
            return
        
        self._do_symmetry(dimensions)
        messagebox.showinfo(self.tr('label_transform'), self.tr('transform_done'))
    
    def _do_symmetry(self, dimensions):
        """Apply symmetry transformation to current pattern"""
        self.save_to_collection()
        for dimension in ["x", "y"]:
            if dimensions[dimension]:
                if dimension == "x":
                    new_cols = self.cols
                    new_rows = self.rows * 2
                    mirror_dim = "y"
                    mirror_dist = self.rows
                else:
                    new_cols = self.cols * 2
                    new_rows = self.rows
                    mirror_dim = "x"
                    mirror_dist = self.cols
                
                new_shapes = self.pattern_shapes.copy()
                for (c, r), shape_type in self.pattern_shapes.items():
                    if mirror_dim == "x":
                        new_shapes[(mirror_dist * 2 - c, r)] = shape_type
                    else:
                        new_shapes[(c, mirror_dist * 2 - r)] = shape_type
                
                new_lines = self.pattern_lines.copy()
                for line in self.pattern_lines:
                    pts = [(mirror_dist * 2 - c, r) if mirror_dim == "x" else (c, mirror_dist * 2 - r) for c, r in line]
                    new_lines.add(frozenset({tuple(pts[0]), tuple(pts[1])}))
                
                new_blocked = self.blocked_nodes.copy()
                for (c, r) in self.blocked_nodes:
                    if mirror_dim == "x":
                        new_blocked.add((mirror_dist * 2 - c, r))
                    else:
                        new_blocked.add((c, mirror_dist * 2 - r))
                
                self.cols, self.rows = new_cols, new_rows
                self.pattern_shapes, self.pattern_lines, self.blocked_nodes = new_shapes, new_lines, new_blocked
                self.ent_cols.delete(0, tk.END); self.ent_cols.insert(0, str(self.cols))
                self.ent_rows.delete(0, tk.END); self.ent_rows.insert(0, str(self.rows))
                self.save_to_collection()
                self.draw_canvas()

    def fill_all_shapes(self):
        """Fill the grid with shapes based on the selected fill style for occupied, free, and loop nodes"""
        
        selected = self.listbox.curselection()
        if len(selected) > 1:  # Multiple patterns selected
            self.apply_settings_to_selection()
            saved_name = self.current_pattern_name
            for idx in selected:
                self.load_pattern_from_collection(self.listbox.get(idx))
                self._do_fill_all_shapes()
            self.load_pattern_from_collection(saved_name)
            messagebox.showinfo(self.tr('label_grid'), self.tr('filling_done'))
            return
        
        self._do_fill_all_shapes()
        messagebox.showinfo(self.tr('label_grid'), self.tr('filling_done'))


    def _do_fill_all_shapes(self):
        def get_dist(p1, p2): return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        def intersect(a, b, c, d):
            def ccw(A, B, C): return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
            return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)
        
        # Remove existing shapes to recompute all shapes
        self.clear_shapes()

        # If outline style is selected for any type of node but not enabled, enable it
        if (self.current_fill_style_occupied == "outline" or self.current_fill_style_free == "outline" or self.current_fill_style_loop == "outline")\
            and not self.use_outlined_shape.get():
            self.toggle_outline()


        # Get occupied node list
        occ = set()
        for r in range(self.rows + 1):
            for c in range(self.cols + 1):
                p = (c, r)
                for line in self.pattern_lines:
                    pts = list(line)
                    if abs((get_dist(p, pts[0]) + get_dist(p, pts[1])) - get_dist(pts[0], pts[1])) < 0.01:
                        occ.add(p); break
                for node in self.blocked_nodes:
                    occ.add(node)
        
        # Get 'outside' nodes to detect loops
        out, stack = set(), []
        for c in range(self.cols + 1): stack.extend([(c, 0), (c, self.rows)])
        for r in range(self.rows + 1): stack.extend([(0, r), (self.cols, r)])
        while stack:
            curr = stack.pop()
            if curr in out or curr in occ: continue
            out.add(curr)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                n = (curr[0] + dx, curr[1] + dy)
                if 0 <= n[0] <= self.cols and 0 <= n[1] <= self.rows:
                    blk = False
                    for line in self.pattern_lines:
                        pts = list(line)
                        if intersect((curr[0]+dx*0.1, curr[1]+dy*0.1), (n[0]-dx*0.1, n[1]-dy*0.1), pts[0], pts[1]):
                            blk = True; break
                    if not blk: stack.append(n)
        
        # Fill with selected fill styles
        for r in range(self.rows + 1):
            for c in range(self.cols + 1):
                p = (c, r)
                
                # Determine node type and apply corresponding fill style
                if p in occ:
                    # Occupied node
                    fill_style = self.current_fill_style_occupied
                elif p in out:
                    # Free node (outside enclosed areas)
                    fill_style = self.current_fill_style_free
                else:
                    # Loop node (inside enclosed areas)
                    fill_style = self.current_fill_style_loop

                # Apply fill style (skip if 'void')
                if fill_style == "plain":
                    self.pattern_shapes[p] = "full"
                elif fill_style == "outline":
                    self.pattern_shapes[p] = "outline"
                # If fill_style == "void", don't add to pattern_shapes

        self.save_to_collection(); 
        self.draw_canvas()
    #--------------------------------------------------------------------------------------------------------

 ###--------------------------------------------------------------------------------------------------------
 ###  MAIN
 ###--------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk(); root.geometry("1400x900"); SVGEditor(root); root.mainloop()
