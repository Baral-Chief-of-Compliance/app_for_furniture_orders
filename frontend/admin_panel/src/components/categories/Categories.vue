<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Категории товаров</div>

               
                <v-container class="d-flex justify-center">
                    <v-col>
                        <v-row class="mx-10">
                            <!-- <v-col  v-for="f in forms_of_work" :key="f.num_work" cols="12" md="3"  v-bind="props_hover">
                                <v-hover v-slot="{ isHovering, props }" >
                                    <v-card  class="mx-auto" height="200" width="300" 
                                        v-bind="props"
                                        :color="isHovering ? 'indigo': undefined"
                                    >
                                        <v-card-item class="text-h6">
                                            {{ f.name_control }}
                                        </v-card-item>
                                    </v-card>

                                    <v-card-actions class="mt-3">
                                        <v-spacer></v-spacer>
                                        <v-btn @click="delete_work(f.num_work)" variant="outlined" color="red"
                                        >Удалить</v-btn>
                                    </v-card-actions>
                                </v-hover>
                            </v-col> -->
                        </v-row>    
                        <v-row class="mx-14 mt-15">
                            <v-btn  block
                                color="green-accent-4"
                                v-bind="props"
                            >
                                Добавить категорию товара
                                </v-btn>
                        </v-row>

                    </v-col>
                </v-container>
            </template>
            <v-card>
                <v-card-title>
                    Форма добавления для категории
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="name_control"
                        label="Название категории"
                        class="mx-5 mb-5"
                    >
                    </v-text-field>
                    <v-text-field v-for="(quantity_categories, categories) in categories"
                        v-model="categories.value"
                        label="Название характеристики"
                        class="mx-5 mb-5"
                        :key="quantity_categories"
                    >
                    </v-text-field>

                </v-form>
                {{ this.categories }}
                    <v-btn color="grey-darken-2" class="mx-5 mb-5" @click="add_category()" >
                        Добавить характеристику
                    </v-btn>
                    <v-btn v-show="show_btn_delet_category" color="red-accent-4" class="mx-5" @click="delete_category()" >
                        Удалить характеристику
                    </v-btn>
                <v-card-actions>
                    <v-btn color="red-accent-4"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green-accent-4"  @click="add_forms_of_work">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>  
    </div>
</template>


<script>
import axios from "axios"

export default{
    data: () => ({
        dialog: false,
        quantity_categories: 1,
        categories: [],
        show_btn_delet_category: false,
    }),
    methods: {
        add_category(){
            this.quantity_categories++
            if (this.quantity_categories === 2){
                this.show_btn_delet_category = true
            }
            this.categories.push({value: ""})
        },
        delete_category(){
            this.quantity_categories--
            if (this.quantity_categories === 1){
                this.show_btn_delet_category = false
            }
        }
    }
}
</script>