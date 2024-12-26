<template>
    <!-- <div class="w-fit absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
        grid gap-4
        md:grid-cols-4
        lg:grid-cols-6
        xl:grid-cols-8">
        <main-card v-for="item in items" :key="item.id"></main-card>
    </div> -->
    <div class="fixed w-full h-full bg-amber-400 flex items-center justify-center flex-col">
        <div class="w-40 h-60 bg-fuchsia-500"></div>
        <div class="w-40 h-16 bg-blue-500 mt-12" @click.stop="test_click"></div>
    </div>
    <div v-if="qian_show" class="fixed z-20 w-full h-full bg-slate-700 flex items-center justify-center">
        <card-con @getCloseStatu="handleCloseStatu"></card-con>
    </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
// import MainCard from '@/components/MainCard.vue';
import CardContent from '@/components/CardContent.vue';

export default defineComponent({
    name: 'MainView',
    components: {
        // 'main-card': MainCard,
        'card-con': CardContent
    },
    setup() {
        const items = Array.from({ length: 0 }, (_, index) => ({
            id: index, // 或者任何其他你想要为每个 div 设置的唯一标识符
            // 其他你需要的数据属性
        }));
        const qian_loading = ref(false);
        const qian_show = ref(false)
        const cardRefs = ref([]);

        return {items, cardRefs,
            qian_loading, qian_show
        };
    },
    methods: {
        test_click() {
            this.qian_show = !this.qian_show;
            return this.qian_show;
        },
        handleCloseStatu(item) {
            console.log(item)
            this.qian_show = false;
        }
    }
})

</script>