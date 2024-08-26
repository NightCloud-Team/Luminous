document.addEventListener('DOMContentLoaded', function() {
    // 选择所有的导航链接，包括子菜单链接
    const navLinks = document.querySelectorAll('.nav-link, .subnav a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault(); // 阻止链接默认的导航行为

            // 移除所有导航链接的激活状态
            navLinks.forEach(lnk => lnk.classList.remove('active'));
            this.classList.add('active'); // 给当前点击的链接添加激活状态

            // 隐藏所有按钮组
            document.querySelectorAll('.group').forEach(group => {
                group.classList.remove('active'); // 使用classList.remove替代style.display设置
            });

            // 显示目标按钮组
            const target = document.querySelector(this.getAttribute('data-target'));
            if (target) {
                target.classList.add('active'); // 使用classList.add替代style.display设置
            }
        });
    });

    // 初始化时显示默认的按钮组
    document.querySelector('.group.active').classList.add('block');
});