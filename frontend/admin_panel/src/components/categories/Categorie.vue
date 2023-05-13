<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">{{ this.name_category }}</div>

                <v-row class="mx-14 mt-15">
                            <v-btn  block
                                color="green-accent-4"
                                v-bind="props"
                            >
                                Добавить товар
                                </v-btn>
                </v-row>
            </template>

            <v-card>
                <v-card-title>
                Форма для добавления товара
                </v-card-title>
                <v-form>
                <v-text-field
                    v-model="name_product"
                    label="Название"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="description_product"
                    label="Описание"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="quantity_product"
                    label="Количество"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="price_product"
                    label="Цена"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="color_product"
                    label="Цвет"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="height_product"
                    label="Высота(см)"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="width_product"
                    label="Ширина(см)"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                <v-text-field
                    v-model="long_product"
                    label="Длинна(см)"
                    color="black"
                    class="mx-5"
                    variant="underlined"
                >
                </v-text-field>

                </v-form>
                <v-card-actions>
                <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                <v-btn color="green"  @click=" add_product()">Добавить</v-btn>
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
        show_btn_delet_category: false,
        name_category: "",
        products: [],
        name_product: "",
        quantity_product: "",
        price_product: "",
        description_product: "",
        color_product: "",
        height_product: "",
        width_product: "",
        long_product: ""
    }),
    mounted(){
        this.get_inf_category()
    },

    updated(){
        this.get_inf_category()
    },
    methods: {
        get_inf_category(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/categories/${this.$route.params.id}`)
            .then(
                response => (
                    this.name_category = response.data.name,
                    this.products = response.data.products
                )
            )
        },

        add_product(){
            axios.post("http://127.0.0.1:5000/admin_panel/api/v1.0/products", 
            {
                id_cat:  this.$route.params.id,
                name_product: this.name_product,
                quantity_product: this.quantity_product,
                price_product: this.price_product,
                description_product: this.description_product,
                color_product: this.color_product,
                height_product: this.height_product,
                width_product: this.width_product,
                long_product: this.long_product
            }
            )
            this.name_product = "",
            this.quantity_product = "",
            this.price_product = "",
            this.description_product = "",
            this.color_product = "",
            this.height_product = "",
            this.width_product = "",
            this.long_product = "",
            this.dialog = false
            
        }
    }
}
</script>