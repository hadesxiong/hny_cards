<template>
    <!-- <div class="w-fit absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
        grid gap-4
        md:grid-cols-4
        lg:grid-cols-6
        xl:grid-cols-8">
        <main-card v-for="item in items" :key="item.id"></main-card>
    </div> -->
    <div class="fixed w-full h-full bg-[url('@/assets/img/home.png')]
        bg-cover bg-center bg-no-repeat">
        <div ref="card_main" class="w-full h-full relative transform-3d
            transition-all ease-in-out duration-1000 top-0 left-1/2 -translate-x-1/2">
            <div ref="card_up" class="bg-white absolute transition-all ease-in-out duration-1000 backface-hidden"
                :class="{ 'z-20': !qian_show, '-z-20': qian_show }">
                <div class="bg-white w-20 h-20"></div>
            </div>
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 transition-all ease-in-out duration-1000 backface-hidden rotate-y-180"
                :class="{ 'z-20': qian_show, '-z-20': !qian_show }">
                <div class="fixed w-full h-full flex items-center justify-center">
                    <card-con @getCloseStatu="handleCloseStatu"></card-con>
                </div>
            </div>
        </div>
        <div class="absolute top-3/4 left-1/2 -translate-x-1/2 -translate-y-1/2
        w-40 h-16 bg-blue-500 mt-12" @click.stop="test_click"></div>
    </div>


</template>

<script>
import { defineComponent, nextTick, ref } from 'vue';
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
        const card_main = ref(null);
        const card_up = ref(null);

        const moveToCenter = () => {
            const rect = card_up.value.getBoundingClientRect();
            console.log(rect);
            const parent_rect = card_up.value.parentNode.getBoundingClientRect();
            console.log(parent_rect);
            const newX = (parent_rect.width - rect.width)/2 + (parent_rect.left - rect.left);
            console.log(newX);
            rect.style.left = `${newX}px`;
        }

        return {
            items, cardRefs, card_main,card_up,
            qian_loading, qian_show, moveToCenter
        };
    },
    methods: {
        // moveToCenter() {
        //     const rect = this.card_up.getBoundingClientRect();
        //     console.log(rect);
        //     const parent_rect = this.card_up.parentNode.getBoundingClientRect();
        //     console.log(parent_rect);
        //     const newX = (parent_rect.width - rect.width)/2 + (parent_rect.left - rect.left);
        //     // container.style.left = '200px';
        //     // container.style.top = '200px';
        //     // rect.left = `${newX}px`;
        //     console.log(newX);
        //     console.log(rect.style);
        //     console.log(rect.left);
        //     // rect.style.left = `${newX}px`;
        // },
        test_click() {
            // this.qian_show = !this.qian_show;
            // return this.qian_show;
            const container = this.card_main;
            container.style.transform = this.qian_show ? 'scale(1)' : 'rotateY(180deg) scale(1)';
            this.moveToCenter();
            nextTick().then(() => {
                // this.moveToCenter();
                // nextTick().then(()=>{
                    this.qian_show = !this.qian_show;
                // })

            })
        },
        handleCloseStatu(item) {
            console.log(item)
            this.qian_show = false;
        }
    }
})

</script>